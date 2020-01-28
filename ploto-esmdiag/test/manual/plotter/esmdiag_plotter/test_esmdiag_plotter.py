# coding: utf-8
import os


def test_esmdiag_plotter():
    task = {
        'metric': 'climo',
        'figure': 'precip',
        "common": {
            "model_info": {
                "id": "FGOALS-g3",
                "atm_id": "GAMIL",
                "ocn_id": "LICOM",
                "ice_id": "CICE"
            },
            "case_info": {
                "id": "gamil_wu_run11"
            },
            "date": {
                "start": "1981-01-01",
                "end": "1981-12-01"
            }
        },
    }
    work_dir = "/home/hujk/clusterfs/wangdp/temp"
    config = {
        "esmdiag": {
            "root": "/home/hujk/ploto/ploto/vendor/esmdiag"
        }
    }

    os.chdir(work_dir)
    from ploto_esmdiag.plotter.esmdiag_plotter import run_plotter
    run_plotter(task, work_dir, config)


if __name__ == "__main__":
    test_esmdiag_plotter()
