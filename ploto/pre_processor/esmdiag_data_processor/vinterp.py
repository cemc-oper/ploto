# coding=utf-8
from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'esmdiag_data_processor',
            'model': 'gamil',
            ...
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()
    model = task["model"]
    if model == 'gamil':
        from ploto.pre_processor.esmdiag_data_processor.models.gamil import vinterp as gamil_vinterp
        gamil_vinterp.run_task(task, work_dir, config)
    else:
        logger.error("model is not supported:", model)
        return False

