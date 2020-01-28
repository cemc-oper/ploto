# coding: utf-8
import time
import warnings


def test_esmdiag():
    warnings.warn("this method needs to be modified", DeprecationWarning)
    common_config = {
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
    }
    task = {
        'steps': [
            {
                'step_type': 'fetcher',
                'common': common_config,
                "type": "ploto.fetcher.local_fetcher",
                "action": "ln",
                "directory": "/home/wangdp/nwpc/earch/ploto/playground/gamil",
                "file_name": "*.nc",
            },
            {
                'step_type': 'processor',
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
                'common': common_config,
            },
            {
                'step_type': 'plotter',
                'type': 'ploto_esmdiag.plotter.esmdiag_plotter',
                'metric': 'climo',
                'figure': 'zonal_mean',
                'common': common_config,
            }
        ]
    }

    message = {
        'app': 'ploto',
        'type': 'ploto',
        'timestamp': time.time(),
        'data': task
    }

    from ploto.scheduler.rabbitmq.producer.producer import send_message
    scheduler_config = {
        'type': 'rabbitmq',
        'server': {
            'host': '10.28.32.114',
            'port': '8672',
        },
        'exchange': 'ploto',
        'queue': 'gidat_plot_task_queue',
        'routing_keys': {
            'pattern': 'plot.task. *',
            'default': 'plot.task.default',
        }
    }
    print('Sending task to scheduler...')
    send_message(message, config=scheduler_config)


if __name__ == "__main__":
    test_esmdiag()
