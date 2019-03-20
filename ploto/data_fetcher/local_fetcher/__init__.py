# coding=utf-8
import pathlib
import os


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


def get_data(file_task, work_dir, config):
    link_local_file(file_task, work_dir)
