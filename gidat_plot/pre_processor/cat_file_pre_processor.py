# coding=utf-8
"""
Cat file.

task schema:
    {
        'type': 'cat_file_pre_processor',
        'file_list': [
            'file_path'
        ]
        'target': 'target file'
    }
"""
import subprocess


def run_pre_processor(task, work_dir, config):
    command = 'cat '
    for a_file_path in task['file_list']:
        command += " {file_path}".format(file_path=a_file_path)
    command += ' > {target}'.format(target=task['target'])
    subprocess.run([command], shell=True)
