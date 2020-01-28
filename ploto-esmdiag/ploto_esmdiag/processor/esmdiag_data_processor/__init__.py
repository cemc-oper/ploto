"""
esmdiag_data_process

task schema:
    {
        'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
        'action: 'vinterp',
        ...
    }
"""
import importlib

from ploto.logger import get_logger
from ploto_esmdiag.processor.esmdiag_data_processor import vinterp

logger = get_logger()


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
    :param work_dir:
    :param config:
        {
            'esmdiag': {
                'root': root dir
            }
        }
    :return:
    """
    action = task["action"]

    try:
        action_module = importlib.import_module('ploto_esmdiag.processor.esmdiag_data_processor.{action}'.format(
            action=action
        ))
    except ImportError:
        logger.error('action is not supported: {action}'.format(action=action))
        return False

    return action_module.run_processor(task, work_dir, config)
