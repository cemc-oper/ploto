# coding: utf-8
from ploto.logger import get_logger
from ploto.step import get_step_module
from ploto.environment import (
    store_base_environment,
    prepare_environment,
    enter_environment,
    recovery_base_environment,
    clear_environment,
    save_task_message
)


logger = get_logger()


def run_ploto(message, config):
    message_data = message['data']
    logger.info('begin plot...')
    base_env = store_base_environment()

    logger.info('prepare environment...')
    work_dir = prepare_environment(config=config)

    logger.info("entering work dir...{work_dir}".format(work_dir=work_dir))
    enter_environment(work_dir)

    # save message
    save_task_message(message_data)

    steps = message_data['steps']
    for step in steps:
        step_module = get_step_module(step)
        if step_module is None:
            logger.error('step module is not found.')
            break
        step_module.run_step(step=step, work_dir=work_dir, config=config)

    logger.info("leaving work dir...{work_dir}".format(work_dir=work_dir))
    recovery_base_environment(base_env)

    logger.info('clearing environment...')
    clear_environment(work_dir, config=config)

    logger.info('end plot')
