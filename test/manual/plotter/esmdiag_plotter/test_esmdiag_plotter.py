# coding: utf-8
import os


def test_esmdiag_plotter():
    task = {
        'metric': 'climo',
        'figure': 'lwcf',
        'common': {
            'model_info': {
                'id': "FGOALS-g3",
                'atm_id': "GAMIL",
                'ocn_id': "LICOM",
                'ice_id': "CICE",
            },
            'case_info': {
                'id': "piControl-bugfix-licom-80368d",
            },
            'date': {
                'start': "0030-01-01",
                'end': "0060-12-31"
            }
        },
    }
    work_dir = "/home/wangdp/nwpc/earch/ploto/playground/gamil"
    config = {
        'esmdiag': {
            'root': '/home/wangdp/nwpc/earch/ploto/ploto/vendor/esmdiag'
        }
    }

    os.chdir(work_dir)
    from ploto.plotter.esmdiag_plotter import run_plotter
    run_plotter(task, work_dir, config)


if __name__ == "__main__":
    test_esmdiag_plotter()
