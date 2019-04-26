# coding=utf-8
"""
Copy files to other location during post processing.

task schema:
    {
        'type': 'copy_file_processor',
        'files': [
            {
                'from': 'source file path',
                'to': 'target file path'
            }
        ]
    }
"""
import pathlib
import shutil
import os


def run_processor(task, work_dir, config):
    files = task['files']
    for file_task in files:
        from_path = pathlib.Path(work_dir, file_task['from'])
        to_path = pathlib.Path(work_dir, file_task['to'])
        if not os.path.exists(to_path.parent):
            os.makedirs(str(to_path.parent))
        shutil.copy2(str(from_path), str(to_path))
