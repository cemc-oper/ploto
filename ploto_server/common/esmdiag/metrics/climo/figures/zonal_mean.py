# coding: utf-8
"""
zonal_mean.py

data requires:
    T.monthly
    U.monthly
    V.monthly
    Q.monthly

"""
from ploto_server.common.esmdiag.metrics.climo.figures import get_common_figure_task


def generate_figure_task(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: 'ice_area',
        }
    :param common_config:
        {
            model_info: {
                id: "FGOALS-g3",
                atm_id: "GAMIL",
                ocn_id: "LICOM",
                ice_id: "CICE",
            },
            case_info: {
                id: "piControl-bugfix-licom-80368d",
            },
            date: {
                start: "0030-01-01",
                end: "0060-12-31"
            }
        }
    :return:
    """
    task = get_common_figure_task(figure_config, common_config)

    task['data_fetcher'] = {
        'type': 'local_fetcher',
        'common': common_config,
    }

    task['pre_processor'] = {
        'type': 'esmdiag_data_processor',
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
    }

    return task
