# coding: utf-8
"""
combined_eof.py

data requires:
    .OLR.daily.anomaly.filtered.
    .U.daily.anomaly.vinterp850:200.filtered.
"""
import datetime

from ploto_server.common.esmdiag.metrics.mjo.util import get_plotter_step, get_gw_step, get_convert_step


def generate_figure_task(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: 'combined_eof',
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
    date_range = [
        (start_date - datetime.timedelta(days=30)).strftime("%Y%m%d"),
        (end_date + datetime.timedelta(days=30)).strftime("%Y%m%d")
    ]

    model_id = common_config['model_info']['id']
    case_id = common_config['case_info']['id']

    file_prefix = '{model_id}.{case_id}'.format(
        model_id=model_id,
        case_id=case_id
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    step1_fields = [
        'FLUTOA',
        'U',
        'PS'
    ]

    steps.extend([
        {
            'step_type': 'fetcher',
            'common': common_config,
            'type': 'edp_fetcher',
            'query_param': {
                'type': 'nc',
                'output_dir': './data',
                'file_prefix': step1_file_prefix,
                'date_range': date_range,
                'field_names': step1_fields,
                'datedif': 'h1'
            },
        }
    ])

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.daily.{time_range}.nc"

    steps.extend([{
        'step_type': 'processor',
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
    } for field in step1_fields])

    steps.append({
        'step_type': 'processor',
        'type': 'cdo_processor',
        'operator': 'chname',
        'params': [
            {
                'old_name': 'FLUTOA',
                'new_name': 'OLR'
            }
        ],
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='FLUTOA'),
        'output_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='OLR'),
    })

    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'anomaly',
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='OLR'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='OLR'),
    })

    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='OLR'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.filtered.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='OLR'),
        'var_name': 'OLR',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })

    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'anomaly',
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='U'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='U'),
    })

    var_file_pattern = "{model}.{case_id}.{name}.daily.anomaly.{start_date}:{end_date}.nc"
    ps_file_path = output_file_pattern.format(
        file_prefix=file_prefix,
        time_range=time_range_string,
        name='PS'
    )
    u_levels = [850, 200]
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'vinterp',
        'model': 'gamil',
        'tasks': [
            {
                "input_file_path": var_file_pattern.format(
                    model=model_id,
                    case_id=case_id,
                    name="U",
                    start_date=common_config["date"]["start"],
                    end_date=common_config["date"]["end"],
                ),
                "ps_file_path": ps_file_path,
                "output_file_path": "{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}.{start_date}:{end_date}.nc".format(
                    model=model_id,
                    case_id=case_id,
                    name='U',
                    levels=":".join([str(level) for level in u_levels]),
                    start_date=common_config["date"]["start"],
                    end_date=common_config["date"]["end"],
                ),
                "var_name": "U",
                "levels": u_levels,
                "interp_type": "linear",
                "extrap": "True"
            },
        ],
        'common': common_config,
    })

    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': "{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}.{start_date}:{end_date}.nc".format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        ),
        'output_file': "{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}.filtered.{start_date}:{end_date}.nc".format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        ),
        'var_name': 'U',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })

    steps.extend(get_gw_step(figure_config, common_config))
    steps.append(get_plotter_step(figure_config, common_config))
    steps.extend(get_convert_step(figure_config, common_config))

    task = {
        'steps': steps
    }

    return task
