"""
local distributor

Copy local files.

task schema:
    {
        'type': 'ploto.distributor.local_distributor',
        'items': [
            {
                'from': 'source file path', # "./*.png"
                'to': 'target file path' # "/plot-dir/task-id
            }
        ]
    }
"""
import shutil
from pathlib import Path
from typing import Dict

from ploto.logger import get_logger


def run_distributor(task: Dict, work_dir: Path, config: Dict):
    logger = get_logger()

    logger.info("run local distributor...")
    for item in task['items']:
        source_files = Path(work_dir).glob(item['from'])
        to_path = Path(work_dir, item['to'])
        if not to_path.parent.exists():
            to_path.parent.mkdir(parents=True)
        for source_file in source_files:
            logger.info(" => copy file {source_file} to {to_path}".format(
                source_file=str(source_file), to_path=str(to_path)
            ))
            shutil.copy2(str(source_file), str(to_path))

    logger.info("run local distributor...done")
    return True
