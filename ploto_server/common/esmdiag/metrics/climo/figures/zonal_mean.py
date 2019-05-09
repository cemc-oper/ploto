# coding: utf-8
"""
zonal_mean.py

data requires:
    T.monthly
    U.monthly
    V.monthly
    Q.monthly

"""
import datetime

from ploto_server.common.esmdiag.metrics.climo.figures import get_plotter_step


def generate_figure_task(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: 'zonal_mean',
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
    task = get_plotter_step(figure_config, common_config)

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
    step2_file_prefix = '{file_prefix}.step2'.format(
        file_prefix=file_prefix
    )

    task['data_fetcher'] = [
        {
            'common': common_config,
            'type': 'edp_fetcher',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': step1_file_prefix,
                'date_range': date_range,
                'field_names': [
                    'T',
                    'U',
                    'V',
                    'Q',
                    'PS'
                ],
                'datedif': 'h0'
            },
        },
        {
            'common': common_config,
            'type': 'edp_fetcher',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': step2_file_prefix,
                'date_range': date_range,
                'field_names': [
                    'gw'
                ],
                'datedif': 'h0'
            }
        }
    ]

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.monthly.{time_range}.nc"

    step1_fields = [
        'T',
        'U',
        'V',
        'Q',
        'PS'
    ]

    task['pre_processor'] = [{
        'type': 'cdo_processor',
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
    } for field in step1_fields]

    task['pre_processor'].append(
        {
            'type': 'cdo_processor',
            'operator': 'select',
            'params': {
                'name': 'gw',
            },
            'input_files': [
                './data/{step2_file_prefix}.*.nc'.format(step2_file_prefix=step2_file_prefix)
            ],
            'output_file': './{file_prefix}.gw.nc'.format(file_prefix=file_prefix),
        }
    )

    task['pre_processor'].append({
        'type': 'esmdiag_data_processor',
        'action': 'vinterp',
        'model': 'gamil',
        'tasks': [
            {
                "var_name": "U",
                "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                "interp_type": "linear",
                "extrap": "False"
            },

            {
                "var_name": "V",
                "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                "interp_type": "linear",
                "extrap": "False"
            },
            {
                "var_name": "Q",
                "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300],
                "interp_type": "linear",
                "extrap": "False"
            },
            {
                "var_name": "T",
                "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                "interp_type": "log",
                "extrap": "False"
            }
        ],
        'common': common_config,
    })

    return task
