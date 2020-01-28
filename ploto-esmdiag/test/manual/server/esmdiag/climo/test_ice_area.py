# coding: utf-8
import json
import uuid


def test_ice_area():
    print("test begin...")

    from ploto_server.common.esmdiag.metrics.climo.figures.ice_area import generate_figure_task

    task = generate_figure_task(
        figure_config={
            'name': 'ice_area',
            'task_id': str(uuid.uuid4())
        },
        common_config={
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
        },
        server_config={
            'esmdiag': {
                'web': {
                    'url': 'http://192.168.212.201:8088',
                    'api': {
                        'task_status': '/api/task/status'
                    },
                    'plot_base_dir': '/home/hujk/clusterfs/wangdp/ploto/plot_base',
                },
            },
        },
    )

    print(json.dumps(task, indent=2))

    from ploto.run import run_ploto
    run_ploto(message={
        'data': task
    }, config={
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
    })


if __name__ == "__main__":
    test_ice_area()
