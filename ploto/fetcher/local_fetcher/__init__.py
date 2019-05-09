# coding=utf-8
import pathlib
import os
import subprocess


def link_local_file(file_task, work_dir):
    """

    :param file_task:
        {
            "type": "local",
            "directory": "/srv/files/ftp/GRAPES_GFS_ORIG_2017070400",
            "file_name": "gmf.gra.2017070400009.grb2",
        },
    :param work_dir:
    :return:
    """

    source_file_path = pathlib.Path(file_task['directory'], file_task['file_name'])
    target_file_path = pathlib.Path(work_dir, file_task['file_name'])
    os.symlink(source_file_path, target_file_path)


def link_file_by_ln(file_task, work_dir):
    """

    :param file_task:
        {
            "type": "local",
            "action": "ln"
            "directory": "/srv/files/ftp/GRAPES_GFS_ORIG_2017070400",
            "file_name": "*.grb2",
        },
    :param work_dir:
    :return:
    """
    subprocess.run(
        [
            "ln -sf {dir}/{file_name} {work_dir}/".format(
                dir=file_task['directory'],
                file_name=file_task['file_name'],
                work_dir=work_dir)
        ],
        shell=True)


def get_data(task, work_dir, config):
    if 'action' in task and task['action'] == 'ln':
        link_file_by_ln(task, work_dir)
    else:
        link_local_file(task, work_dir)
