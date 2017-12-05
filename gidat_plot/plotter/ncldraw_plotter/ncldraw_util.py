# coding=utf-8
import json
import subprocess
import pathlib
import xml.etree.cElementTree as ET


def change_task_file(task_file, work_dir):
    task_file_name = pathlib.Path(task_file).name

    tree = ET.parse(task_file)
    root = tree.getroot()

    work_station_node = root.find("./workstation")
    output_path = work_station_node.get('output')
    output_path = pathlib.Path(work_dir, output_path)
    work_station_node.set('output', str(output_path))

    changed_task_file_path = str(pathlib.Path(work_dir, task_file_name))
    tree.write(changed_task_file_path)

    return changed_task_file_path


def run_plotter(plotter_task, work_dir, config):
    print('prepare plot...')

    changed_task_file_path = change_task_file(plotter_task['task_file'], work_dir)

    param = {
        'task_file': changed_task_file_path,
        'time_level': plotter_task['time_level']
    }
    print('running ncldraw...')

    command = ['/bin/bash', '-i', '-c', 'ncldraw {task_file} {time_level}'.format(
        task_file=param['task_file'],
        time_level=param['time_level']
    )]
    print(command)

    ncldraw_result = subprocess.run(
        command
    )
    print(ncldraw_result.stdout)
    print(ncldraw_result.stderr)

    print('running ncldraw...done')
