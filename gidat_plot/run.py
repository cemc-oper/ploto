# coding: utf-8
import uuid
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from gidat_plot.data_fetcher import prepare_data
from gidat_plot.plotter import draw_plot
from gidat_plot.post_processor import do_post_processing
from gidat_plot.logger import get_logger


def prepare_environment(config):
    base_config = config['base']
    run_base_dir = base_config['run_base_dir']

    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    os.makedirs(work_dir)
    return work_dir


def clear_environment(work_dir, config):
    pass


def run_gidat_plot(message, config):
    logger = get_logger()
    logger.info('begin plot...')
    current_directory = os.getcwd()

    logger.info('prepare environment...')
    work_dir = prepare_environment(config=config)

    logger.info("entering work dir: {work_dir}".format(work_dir=work_dir))
    os.chdir(work_dir)

    logger.info('prepare data...')
    files = message['data']['files']
    prepare_data(files, work_dir, config=config)

    logger.info('drawing plot...')
    draw_plot(message['data']['plotter'], work_dir, config=config)

    logger.info('doing post processing...')
    do_post_processing(message['data']['post_processor'], work_dir, config=config)

    logger.info('leaving work_dir...')
    os.chdir(current_directory)

    logger.info('clearing environment...')
    clear_environment(work_dir, config=config)

    logger.info('end plot')
