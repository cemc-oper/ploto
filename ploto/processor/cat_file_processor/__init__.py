"""
Cat file.

task schema:
    {
        'type': 'ploto.processor.cat_file_processor',
        'file_list': [
            'file_path'
        ]
        'target': 'target file'
    }
"""
import subprocess
from pathlib import Path
from typing import Dict


def run_processor(task: Dict, work_dir: Path, config: Dict):
    command = 'cat '
    for a_file_path in task['file_list']:
        file_path = str(Path(work_dir, a_file_path))
        command += " {file_path}".format(file_path=file_path)

    target_file_path = str(Path(work_dir, task['target']))
    command += ' > {target}'.format(target=target_file_path)

    subprocess.run([command], shell=True)
