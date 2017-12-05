# coding: utf-8
import uuid
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from gidat_plot.plotter.ncl_plotter import ncl_script_util
from gidat_plot.plotter.ncldraw_plotter import ncldraw_util
from gidat_plot.data_fetcher import ftp_fetcher, local_fetcher, ddps_fetcher


def prepare_environment(config):
    base_config = config['base']
    run_base_dir = base_config['run_base_dir']

    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    os.makedirs(work_dir)
    os.chdir(work_dir)
    return work_dir


def prepare_data(files, work_dir, config):
    os.chdir(work_dir)
    for file_task in files:
        file_type = file_task['type']
        if file_type == 'ftp':
            ftp_fetcher.get_data(file_task, work_dir)
        elif file_type == 'local':
            local_fetcher.get_data(file_task, work_dir)
        elif file_type == 'ddps':
            ddps_fetcher.get_data(file_task, work_dir, config)
        else:
            print("file type not supported:", file_type)


def draw_plot(plotter_task, work_dir, config):
    if plotter_task['type'] == 'ncl_plotter':
        ncl_script_util.run_plotter(plotter_task, work_dir)
    elif plotter_task['type'] == 'ncldraw_plotter':
        ncldraw_util.run_plotter(plotter_task, work_dir, config=config)
    else:
        print("plotter type is not supported:", plotter_task['type'])


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
