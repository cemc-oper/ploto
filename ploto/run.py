# coding: utf-8
from ploto.fetcher import run_fetcher
from ploto.plotter import draw_plot
from ploto.processor import do_processing
from ploto.logger import get_logger
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

    if 'data_fetcher' in message_data:
        logger.info('prepare data...')
        run_fetcher(message_data['data_fetcher'], work_dir, config=config)

    if 'pre_processor' in message_data:
        logger.info('doing pre processing...')
        do_processing(message_data['pre_processor'], work_dir, config=config)

    if 'plotter' in message_data:
        logger.info('drawing plot...')
        draw_plot(message_data['plotter'], work_dir, config=config)

    if 'post_processor' in message_data:
        logger.info('doing post processing...')
        do_processing(message_data['post_processor'], work_dir, config=config)

    logger.info("leaving work dir...{work_dir}".format(work_dir=work_dir))
    recovery_base_environment(base_env)

    logger.info('clearing environment...')
    clear_environment(work_dir, config=config)

    logger.info('end plot')
