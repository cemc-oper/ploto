# coding: utf-8
import os


def test_filter():
    from ploto_esmdiag.processor.esmdiag_data_processor import run_processor
    task = {
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
        'action': 'filter',
        'input_file': 'GAMIL.gamil_wu_run11.OLR.daily.anomaly.1979-01-01:1980-12-31.nc',
        'output_file': 'GAMIL.gamil_wu_run11.OLR.daily.anomaly.filtered.1979-01-01:1980-12-31.nc',
        'var_name': 'OLR',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
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
    test_filter()
