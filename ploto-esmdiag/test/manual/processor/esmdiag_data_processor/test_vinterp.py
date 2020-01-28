# coding: utf-8
import os


def test_vinterp():
    import warnings
    warnings.warn("vinterp task has changed.", DeprecationWarning)

    from ploto_esmdiag.processor.esmdiag_data_processor.vinterp.models.gamil import run_task
    task = {
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
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
    }
    config = {
        'esmdiag': {
            'root': '/home/wangdp/nwpc/earch/ploto/ploto/vendor/esmdiag'
        }
    }
    work_dir = "/home/wangdp/nwpc/earch/ploto/playground/gamil"
    os.chdir(work_dir)
    run_task(
        task,
        work_dir,
        config
    )


if __name__ == "__main__":
    test_vinterp()
