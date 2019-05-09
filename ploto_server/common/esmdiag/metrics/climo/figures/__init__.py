# coding: utf-8


def get_plotter_step(figure_config, common_config) -> dict:
    """

    :param figure_config:
        {
            name: '...',
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
    task = {
        'step_type': 'plotter',
        'type': 'esmdiag_plotter',
        'metric': 'climo',
        'figure': figure_config["name"],
        'common': common_config,
    }
    return task
