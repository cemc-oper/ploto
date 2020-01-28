# coding=utf-8
import importlib

from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
            'model': 'gamil',
            'tasks': [
                {
                    "input_file_path": "",
                    "ps_file_path": "",
                    "output_file_path": "",
                    "var_name": "U",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false",
                },
            ],
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()
    model = task["model"]
    try:
        vinterp_module = importlib.import_module(".models.{model}.vinterp".format(model=model), __package__)
        return vinterp_module.run_task(task, work_dir, config)
    except ImportError:
        logger.error("model is not supported: {model}".format(model=model))
        return False
