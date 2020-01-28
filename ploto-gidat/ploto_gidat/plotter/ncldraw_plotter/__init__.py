# coding=utf-8
import subprocess
import pathlib
import xml.etree.cElementTree as ET

from ploto.logger import get_logger


def generate_task_file(task_file_config, work_dir):
    task_file_path = task_file_config['file_path']
    task_file_content = task_file_config['file_content']

    task_file_name = pathlib.Path(task_file_path).name

    root = ET.fromstring(task_file_content)

    work_station_node = root.find("./workstation")
    output_path = work_station_node.get('output')
    output_path = pathlib.Path(work_dir, output_path)
    work_station_node.set('output', str(output_path))

    for plot_node in root.findall(".//*[@datadir]"):
        data_dir = plot_node.get('datadir')
        data_dir = pathlib.Path(work_dir)
        plot_node.set('datadir', str(data_dir))

    changed_task_file_path = str(pathlib.Path(work_dir, task_file_name))
    tree = ET.ElementTree(root)
    tree.write(changed_task_file_path)

    return changed_task_file_path


def generate_resource_file(resource_file_config, config):
    resource_base_dir = config['ncldraw_plotter']['resource_base_dir']
    file_path = resource_file_config['file_path']
    file_content = resource_file_config['file_content']

    resource_file_path = pathlib.Path(resource_base_dir, file_path)
    with open(resource_file_path) as f:
        f.write(file_content)


def run_plotter(plotter_task, work_dir, config):
    """
    run ncldraw plotter

    :param plotter_task: a dict config of plotter task.
        {
            'type': 'ploto.plotter.ncldraw_plotter',
            'task_files': [
                {
                    'file_path': 'task.xml',
                    'file_content': 'task file content'
                }
            ],
            'resource_files':[
                {
                    'file_path': 'fill.xml', # resource file path, NOTE: this is a relative path currently.
                    'file_content': 'content', # resource file content
                }
            ],
            'time_level': '2017071400084', # YYYYMMDDHH + HHH, used by ncldraw program.
            'image_path': 'image.png', # image file path
        }
    :param work_dir:
    :param config:
    :return:
    """

    logger = get_logger()
    logger.info('prepare plot...')

    # resource file
    if 'resource_files' in plotter_task:
        for a_resource_file_config in plotter_task['resource_files']:
            generate_resource_file(a_resource_file_config, config)

    # task file
    cur_index = 0

    for a_task_file_config in plotter_task['task_files']:
        logger.info('task {cur_index}:'.format(cur_index=cur_index))
        changed_task_file_path = generate_task_file(a_task_file_config, work_dir)

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
        logger.info('task {cur_index}: done'.format(cur_index=cur_index))

    logger.info('running ncldraw...done')
