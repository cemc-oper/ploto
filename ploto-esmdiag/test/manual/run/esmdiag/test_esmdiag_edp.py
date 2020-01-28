# coding: utf-8
import time


def test_esmdiag_edp():
    """
    test A climo/precip ESMDiag task using data from EDP(earth data platform)
    """
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
            'start': "1981-01-01",
            'end': "1981-12-01"
        }
    }
    task = {
        'steps': [
            {
                'step_type': 'fetcher',
                'common': common_config,
                'type': 'ploto_esmdiag.fetcher.edp_fetcher',
                'query_param': {
                    'type': 'nc',
                    'output_dir': './data',
                    'file_prefix': 'GAMIL.gamil_wu_run11.step1',
                    'date_range': ['19810101', '19820101'],
                    'field_names': [
                        'PRECT',
                        'PRECC',
                        'PRECL',
                        'PS'
                    ],
                    'datedif': 'h0'
                },
            },
            {
                'step_type': 'fetcher',
                'common': common_config,
                'type': 'ploto_esmdiag.fetcher.edp_fetcher',
                'query_param': {
                    'type': 'nc',
                    'output_dir': './data',
                    'file_prefix': 'GAMIL.gamil_wu_run11.step2',
                    'date_range': ['19820101', '19820101'],
                    'field_names': [
                        'gw'
                    ],
                    'datedif': 'h0'
                }
            },
            {
                'step_type': 'processor',
                'type': 'ploto.processor.cdo_processor',
                'operator': 'select',
                'params': {
                    'name': 'PS',
                    'startdate': '1981-01-01',
                    'enddate': '1981-12-01'
                },
                'input_files': [
                    './data/GAMIL.gamil_wu_run11.step1.*.nc'
                ],
                'output_file': './GAMIL.gamil_wu_run11.PS.monthly.1981-01-01:1981-12-01.nc',
            },

            {
                'step_type': 'processor',
                'type': 'ploto.processor.cdo_processor',
                'operator': 'select',
                'params': {
                    'name': 'PRECT',
                    'startdate': '1981-01-01',
                    'enddate': '1981-12-01'
                },
                'input_files': [
                    './data/GAMIL.gamil_wu_run11.step1.*.nc'
                ],
                'output_file': './GAMIL.gamil_wu_run11.PRECT.monthly.1981-01-01:1981-12-01.nc',
            },
            {
                'step_type': 'processor',
                'type': 'ploto.processor.cdo_processor',
                'operator': 'select',
                'params': {
                    'name': 'PRECC',
                    'startdate': '1981-01-01',
                    'enddate': '1981-12-01'
                },
                'input_files': [
                    './data/GAMIL.gamil_wu_run11.step1.*.nc'
                ],
                'output_file': './GAMIL.gamil_wu_run11.PRECC.monthly.1981-01-01:1981-12-01.nc',
            },

            {
                'step_type': 'processor',
                'type': 'ploto.processor.cdo_processor',
                'operator': 'select',
                'params': {
                    'name': 'PRECL',
                    'startdate': '1981-01-01',
                    'enddate': '1981-12-01'
                },
                'input_files': [
                    './data/GAMIL.gamil_wu_run11.step1.*.nc'
                ],
                'output_file': './GAMIL.gamil_wu_run11.PRECL.monthly.1981-01-01:1981-12-01.nc',
            },
            {
                'step_type': 'processor',
                'type': 'ploto.processor.cdo_processor',
                'operator': 'select',
                'params': {
                    'name': 'gw',
                },
                'input_files': [
                    './data/GAMIL.gamil_wu_run11.step2.*.nc'
                ],
                'output_file': './FGOALS-g3.gamil_wu_run11.gw.nc',
            },
            {
                'step_type': 'plotter',
                'type': 'ploto_esmdiag.plotter.esmdiag_plotter',
                'metric': 'climo',
                'figure': 'precip',
                'common': common_config,
            },
        ],
    }

    message = {
        'app': 'ploto',
        'type': 'ploto',
        'timestamp': time.time(),
        'data': task
    }

    config = {
        'base': {
            'run_base_dir': '/home/hujk/clusterfs/wangdp/ploto/run_base',
            'python_exe': '/home/hujk/.pyenv/versions/ploto-env/bin/python3'
        },
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/pyProject/"
        },
        'esmdiag': {
            'root': '/home/hujk/ploto/ploto/vendor/esmdiag'
        }
    }

    from ploto.run import run_ploto
    run_ploto(message, config)


if __name__ == "__main__":
    test_esmdiag_edp()
