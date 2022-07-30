from typing import Dict

from ploto.logger import get_logger
from ploto.step import run_steps
from ploto.environment import (
    store_base_environment,
    prepare_environment,
    enter_environment,
    recovery_base_environment,
    clear_environment,
    save_task_message
)


logger = get_logger()


def run_ploto(message: Dict, config: Dict):
    message_data = message['data']
    logger.info('begin plot...')
    base_env = store_base_environment()

    logger.info('prepare environment...')
    work_dir = prepare_environment(config=config)

    logger.info(f"entering work dir...{work_dir}")
    enter_environment(work_dir)

    # save message
    save_task_message(message_data)

    steps = message_data['steps']
    _ = run_steps(steps, work_dir, config)

    logger.info(f"leaving work dir...{work_dir}")
    recovery_base_environment(base_env)

    logger.info('clearing environment...')
    clear_environment(work_dir, config=config)

    logger.info('end plot')
