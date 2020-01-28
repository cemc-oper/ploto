# coding: utf-8
import os


def test_detrend():
    from ploto_esmdiag.processor.esmdiag_data_processor import run_processor
    task = {
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'input_file': 'GAMIL.gamil_wu_run11.PRC.daily.anomaly.area_avg_IO.1992-01-01:1993-12-31.nc',
        'var_name': 'PRC',
        'output_file': 'GAMIL.gamil_wu_run11.PRC.daily.anomaly.area_avg_IO.detrended.1992-01-01:1993-12-31.nc',
        'common_config': {
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
                'start': "1979-01-01",
                'end': "1980-12-01"
            }
        }
    }
    config = {
        'esmdiag': {
            'root': '/home/hujk/ploto/ploto/vendor/esmdiag'
        }
    }
    work_dir = "/home/hujk/clusterfs/wangdp/temp/temp"
    os.chdir(work_dir)
    run_processor(
        task,
        work_dir,
        config
    )


if __name__ == "__main__":
    test_detrend()
