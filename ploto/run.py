# coding: utf-8
import uuid
import os
import json

from ploto.fetcher import run_fetcher
from ploto.plotter import draw_plot
from ploto.processor import do_processing
from ploto.logger import get_logger


def get_work_dir(config):
    base_config = config['base']
    run_base_dir = base_config['run_base_dir']

    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    try:
        os.makedirs(work_dir)
    except FileExistsError as e:
        logger = get_logger()
        logger.warn('directory already exists:', work_dir)
    return work_dir


def prepare_environment(config):
    return get_work_dir(config)


def clear_environment(work_dir, config):
    pass


def run_ploto(message, config):
    message_data = message['data']
    logger = get_logger()
    logger.info('begin plot...')
    current_directory = os.getcwd()

    logger.info('prepare environment...')
    work_dir = prepare_environment(config=config)

    logger.info("entering work dir: {work_dir}".format(work_dir=work_dir))
    os.chdir(work_dir)

    # save message
    with open('message.json', 'w') as f:
        content = json.dumps(message_data, indent=2)
        f.write(content)

    logger.info('prepare data...')
    files = message_data['data_fetcher']
    run_fetcher(files, work_dir, config=config)

    logger.info('doing pre processing...')
    if 'pre_processor' in message_data:
        do_processing(message_data['pre_processor'], work_dir, config=config)

    logger.info('drawing plot...')
    draw_plot(message_data['plotter'], work_dir, config=config)

    logger.info('doing post processing...')
    if 'post_processor' in message_data:
        do_processing(message_data['post_processor'], work_dir, config=config)

    logger.info('leaving work_dir...')
    os.chdir(current_directory)

    logger.info('clearing environment...')
    clear_environment(work_dir, config=config)

    logger.info('end plot')
