# coding=utf-8
import subprocess
import pathlib
import xml.etree.cElementTree as ET

from gidat_plot.logger import get_logger


def change_task_file(task_file, work_dir):
    task_file_name = pathlib.Path(task_file).name

    tree = ET.parse(task_file)
    root = tree.getroot()

    work_station_node = root.find("./workstation")
    output_path = work_station_node.get('output')
    output_path = pathlib.Path(work_dir, output_path)
    work_station_node.set('output', str(output_path))

    for plot_node in root.findall(".//plot[@datadir]"):
        data_dir = plot_node.get('datadir')
        data_dir = pathlib.Path(work_dir, data_dir)
        plot_node.set('datadir', str(data_dir))

    changed_task_file_path = str(pathlib.Path(work_dir, task_file_name))
    tree.write(changed_task_file_path)

    return changed_task_file_path


def run_plotter(plotter_task, work_dir, config):

    logger = get_logger()
    logger.info('prepare plot...')

    changed_task_file_path = change_task_file(plotter_task['task_file'], work_dir)

    param = {
        'task_file': changed_task_file_path,
        'time_level': plotter_task['time_level']
    }
    logger.info('running ncldraw...')

    command = ['ncldraw {task_file} {time_level}'.format(
        task_file=param['task_file'],
        time_level=param['time_level']
    )]
    # print(command)

    ncldraw_result = subprocess.run(
        command,
        shell=True
    )
    # logger.debug(ncldraw_result.stdout)
    # logger.debug(ncldraw_result.stderr)

    logger.info('running ncldraw...done')
