# coding=utf-8
from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'esmdiag_data_processor',
            'model': 'gamil',
            'tasks': [
                {
                    "var_name": "U",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false"
                },

                {
                    "var_name": "V",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false"
                },
                {
                    "var_name": "Q",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300],
                    "interp_type": "linear",
                    "extrap": "false"
                },
                {
                    "var_name": "T",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "log",
                    "extrap": "false"
                }
            ],
            common: {
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
            },
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()
    model = task["model"]
    if model == 'gamil':
        from ploto.processor.esmdiag_data_processor.models.gamil import vinterp as gamil_vinterp
        return gamil_vinterp.run_task(task, work_dir, config)
    else:
        logger.error("model is not supported:", model)
        return False

