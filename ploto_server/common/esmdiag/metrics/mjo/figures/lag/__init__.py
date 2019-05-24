# coding: utf-8
"""
lag.py

data requires:
    .PRC.daily.anomaly.area_avg_IO.detrended.
    .PRC.daily.anomaly.area_avg_IO.detrended.filtered.
    .PRC.daily.anomaly.lat_avg_lon_band.detrended.
    .PRC.daily.anomaly.lat_avg_lon_band.detrended.filtered.
    .PRC.daily.anomaly.lon_avg_lat_band.detrended.
    .PRC.daily.anomaly.lon_avg_lat_band.detrended.filtered.
    .U.daily.anomaly.vinterp850:200.lat_avg_lon_band.detrended.
    .U.daily.anomaly.vinterp850:200.lat_avg_lon_band.detrended.filtered.
    .U.daily.anomaly.vinterp850:200.lon_avg_lat_band.detrended.
    .U.daily.anomaly.vinterp850:200.lon_avg_lat_band.detrended.filtered.
"""
import datetime

from ploto_server.common.esmdiag.metrics.mjo.util import get_plotter_step, get_gw_step


def generate_figure_task(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: 'lag',
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

    steps.extend(get_gw_step(figure_config, common_config))

    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [
        (start_date - datetime.timedelta(days=30)).strftime("%Y%m%d"),
        (end_date + datetime.timedelta(days=30)).strftime("%Y%m%d")
    ]

    model_id = common_config['model_info']['atm_id']
    case_id = common_config['case_info']['id']

    file_prefix = '{model_id}.{case_id}'.format(
        model_id=model_id,
        case_id=case_id
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    step1_fields = [
        'PRECT',
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
                'old_name': 'PRECT',
                'new_name': 'PRC'
            }
        ],
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRECT'),
        'output_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
    })

    from . import prc
    steps.extend(prc.generate_steps(file_prefix, output_file_pattern, time_range_string, common_config))

    # U
    from . import u
    steps.extend(u.generate_steps(
        file_prefix, output_file_pattern, time_range_string, common_config, model_id, case_id))

    steps.append(get_plotter_step(figure_config, common_config))

    task = {
        'steps': steps
    }

    return task
