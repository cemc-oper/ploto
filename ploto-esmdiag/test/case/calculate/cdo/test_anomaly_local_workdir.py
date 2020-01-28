# coding: utf-8
import json
import datetime


def test_anomaly():
    print("test begin...")

    common_config = {
        'model_info': {
            'id': "FGOALS-g3",
            'atm_id': "GAMIL",
            'ocn_id': "LICOM",
            'ice_id': "CICE",
        },
        'case_info': {
            'id': "gamil_wu_run11",
        },
        'date': {
            'start': "1982-01-01",
            'end': "1992-12-31"
        },
    }

    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [
        (start_date - datetime.timedelta(days=30)).strftime("%Y%m%d"),
        (end_date + datetime.timedelta(days=30)).strftime("%Y%m%d")
    ]

    steps = []

    steps.append({
        'step_type': 'fetcher',
        'common': common_config,
        "type": "ploto.fetcher.local_fetcher",
        "action": "ln",
        "directory": "/home/hujk/clusterfs/GAMIL",
        "file_name": "gamil_wu_run11.gamil.h1.*.nc",
        "output_directory": "./data"
    })

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.daily.{time_range}.nc"

    steps.append({
        'step_type': 'processor',
        'type': 'ploto.processor.cdo_processor',
        'operator': 'select',
        'params': {
            'name': 'U',
            'startdate': common_config['date']['start'],
            'enddate': common_config['date']['end']
        },
        'input_files': [
            './data/gamil_wu_run11.gamil.h1.*.nc'.format(step1_file_prefix='step1.')
        ],
        'output_file': output_file_pattern.format(
            file_prefix='step2.',
            time_range=time_range_string,
            name='U',
        ),
    })

    steps.append({
        'step_type': 'processor',
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
        'action': 'anomaly',
        'input_file': output_file_pattern.format(
            file_prefix='step2.',
            time_range=time_range_string,
            name='U'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix='step3.',
            time_range=time_range_string,
            name='U'),
    })

    from ploto.run import run_ploto
    run_ploto(message={
        'data': {
            'steps': steps
        }
    }, config={
        'base': {
            'run_base_dir': '/home/hujk/ploto/run_base',
            'python_exe': '/home/hujk/.pyenv/versions/ploto-env/bin/python3'
        },
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/clusterfs/wangdp/pyProject"
        },
        'esmdiag': {
            'root': '/home/hujk/ploto/ploto/vendor/esmdiag'
        }
    })


if __name__ == "__main__":
    test_anomaly()
