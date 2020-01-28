# coding: utf-8
import os


def test_lon_avg():
    from ploto_esmdiag.processor.esmdiag_data_processor import run_processor
    task = {
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
        'action': 'lon_avg',
        'start_lon': 80.0,
        'end_lon': 100.0,
        'input_file': 'GAMIL.gamil_wu_run11.U.daily.anomaly.vinterp850:200.1979-01-01:1980-12-01.nc',
        'var_name': 'U',
        'output_file': 'GAMIL.gamil_wu_run11.U.daily.anomaly.vinterp850:200.lon_avg_lat_band.1979-01-01:1980-12-01.nc',

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
    test_lon_avg()
