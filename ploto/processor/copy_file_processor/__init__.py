"""
Copy files to other location during post processing.

task schema:
    {
        'type': 'ploto.processor.copy_file_processor',
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
from pathlib import Path
from typing import Dict


from ploto.logger import get_logger


logger = get_logger()


def run_processor(task: Dict, work_dir: Path, config: Dict):
    files = task['files']
    for file_task in files:
        from_path = pathlib.Path(work_dir, file_task['from'])
        to_path = pathlib.Path(work_dir, file_task['to'])
        if not to_path.parent.exists():
            to_path.parent.mkdir(parents=True, exist_ok=True)
        logger.debug(f"copy file: {from_path} => {to_path}")
        shutil.copy2(str(from_path), str(to_path))
