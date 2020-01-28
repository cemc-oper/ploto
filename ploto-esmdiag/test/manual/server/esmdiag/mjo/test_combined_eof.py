# coding: utf-8
import json
import uuid


def test_combined_eof():
    print("test begin...")

    from ploto_server.common.esmdiag.metrics.mjo.figures.combined_eof import generate_figure_task

    task = generate_figure_task(
        figure_config={
            'name': 'combined_eof',
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
                'start': "1992-01-01",
                'end': "1993-12-31"
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
    test_combined_eof()
