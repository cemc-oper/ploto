# coding=utf-8
import pathlib
import shutil
import os


def run_post_processor(task, work_dir, config):
    files = task['files']
    for file_task in files:
        from_path = pathlib.Path(work_dir, file_task['from'])
        to_path = pathlib.Path(work_dir, file_task['to'])
        os.makedirs(str(to_path.parent))
        shutil.copy2(str(from_path), str(to_path))
