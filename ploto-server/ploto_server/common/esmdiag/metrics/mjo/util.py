# coding: utf-8
import datetime


def get_plotter_step(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: '...',
        }
    :param common_config:
        {
            model_info: {
                id: "GAMIL",
                atm_id: "GAMIL",
                ocn_id: "LICOM",
                ice_id: "CICE",
            },
            case_info: {
                id: "piControl-bugfix-licom-80368d",
            },
            date: {
                start: "0030-01-01",
                end: "0060-12-31"
            }
        }
    :return:
    """
    task = {
        'step_type': 'plotter',
        'type': 'ploto.plotter.esmdiag_plotter',
        'metric': 'mjo',
        'figure': figure_config["name"],
        'common': common_config,
    }
    return task


def get_gw_step(figure_config, common_config):
    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    step2_file_prefix = '{model_id}.{case_id}.step2'.format(
        model_id=common_config['model_info']['id'],
        case_id=common_config['case_info']['id']
    )

    step2_fields = [
        'gw'
    ]

    steps = [
        {
            'step_type': 'fetcher',
            'common': common_config,
            'type': 'ploto_esmdiag.fetcher.edp_fetcher',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': step2_file_prefix,
                'date_range': date_range,
                'field_names': step2_fields,
                'datedif': 'h0'
            }
        },
        {
            'step_type': 'processor',
            'type': 'cdo_processor',
            'operator': 'select',
            'params': {
                'name': 'gw',
            },
            'input_files': [
                './data/{step2_file_prefix}.*.nc'.format(step2_file_prefix=step2_file_prefix)
            ],
            'output_file': './{model_id}.{case_id}.gw.nc'.format(
                model_id=common_config['model_info']['atm_id'],
                case_id=common_config['case_info']['id']),
        }
    ]

    return steps


def get_convert_step(figure_config, common_config):
    steps = [
        {
            'step_type': 'processor',
            'type': 'ploto.processor.convert_processor',
            'operator': 'general',
            'params': [
                '-density 300',
                '-set filename:f "%t"',
                '*.pdf',
                '%[filename:f].png'
            ]
        }
    ]

    return steps