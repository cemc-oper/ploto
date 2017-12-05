# coding: utf-8
import uuid
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from gidat_plot.data_fetcher import prepare_data
from gidat_plot.plotter import draw_plot


def prepare_environment(config):
    base_config = config['base']
    run_base_dir = base_config['run_base_dir']

    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    os.makedirs(work_dir)
    print("entering work dir:", work_dir)
    os.chdir(work_dir)
    return work_dir


def clear_environment(work_dir):
    pass


def run_gidat_plot(message, config):
    print('begin plot...')
    current_directory = os.getcwd()

    print('prepare environment...')
    work_dir = prepare_environment(config=config)

    print('prepare data...')
    files = message['data']['files']
    prepare_data(files, work_dir, config=config)

    print('drawing plot...')
    draw_plot(message['data']['plotter'], work_dir, config=config)

    print('clearing environment...')
    clear_environment(work_dir)

    os.chdir(current_directory)
    print('end plot')
