# coding: utf-8
"""
precip

data requires:
    PRECT.monthly
    PRECC.monthly
    PRECL.monthly

"""
from ploto_server.common.esmdiag.metrics.climo.figures import get_common_figure_task


def generate_figure_task(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: 'precip',
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

    task['data_fetcher'] = [
        {
            'type': 'local_fetcher',
            'common': common_config,
        }
    ]

    return task
