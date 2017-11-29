# coding=utf-8
import pathlib
import os


def link_local_file(file_task, work_dir):
    source_file_path = pathlib.Path(file_task['directory'], file_task['file_name'])
    target_file_path = pathlib.Path(work_dir, file_task['file_name'])
    os.symlink(source_file_path, target_file_path)


def get_data(file_task, work_dir):
    link_local_file(file_task, work_dir)
