# coding: utf-8
"""
swcf

data requires:
    SWCF.monthly

"""
import datetime

from ploto_server.common.esmdiag.metrics.climo.util import get_plotter_step, get_gw_step, get_convert_step
from ploto_server.common.esmdiag.esmdiag_server import get_send_status_steps, TaskStatus, get_local_distribution_steps


def generate_figure_task(figure_config, common_config, server_config) -> dict:
    """

    :param figure_config:
        {
            name: 'swcf',
        }
    :param common_config:
        {
            model_info: {
                id: "FGOALS-g3",
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
    steps = []

    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    file_prefix = '{atm_id}.{case_id}'.format(
        atm_id=common_config['model_info']['atm_id'],
        case_id=common_config['case_info']['id']
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    steps.extend([
        {
            'step_type': 'fetcher',
            'common': common_config,
            'type': 'ploto_esmdiag.fetcher.edp_fetcher',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': step1_file_prefix,
                'date_range': date_range,
                'field_names': [
                    'SWCF',
                ],
                'datedif': 'h0'
            },
        }
    ])

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.monthly.{time_range}.nc"

    step1_fields = [
        'SWCF',
    ]

    steps.extend([{
        'step_type': 'processor',
        'type': 'ploto.processor.cdo_processor',
        'operator': 'select',
        'params': {
            'name': field,
            'startdate': common_config['date']['start'],
            'enddate': common_config['date']['end']
        },
        'input_files': [
            './data/{step1_file_prefix}.*.nc'.format(step1_file_prefix=step1_file_prefix)
        ],
        'output_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name=field,
        ),
    } for field in step1_fields])

    steps.extend(get_gw_step(figure_config, common_config))
    steps.append(get_plotter_step(figure_config, common_config))
    steps.extend(get_convert_step(figure_config, common_config))
    steps.extend(get_local_distribution_steps(figure_config, common_config, server_config))
    steps.extend(get_send_status_steps(TaskStatus.Complete, figure_config, common_config, server_config))

    task = {
        'steps': steps
    }

    return task
