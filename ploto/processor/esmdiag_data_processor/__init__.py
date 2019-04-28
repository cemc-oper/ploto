"""
esmdiag_data_process

task schema:
    {
        'type': 'esmdiag_data_processor',
        'action: 'vinterp',
        ...
    }
"""

from ploto.logger import get_logger
from ploto.processor.esmdiag_data_processor import vinterp

action_map = {
    'vinterp': vinterp
}

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
    action_processor = action_map.get(action, None)
    if action_processor is None:
        logger.error("action type not supported:", action)
        return False

    return action_processor.run_processor(task, work_dir, config)
