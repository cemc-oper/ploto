"""
cdo chname

task schema:
    {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'chname',
        'params': [
            {
                'old_name': 'FLUTOA',
                'new_name': 'OLR'
            }
        ],
        'input_file': './data/GAMIL.gamil_wu_run11.FLUTOA.daily.1979-01-01:1980-12-31.nc',
        'output_file': './data/GAMIL.gamil_wu_run11.OLR.daily.1979-01-01:1980-12-31.nc',
    }
"""
import subprocess
from pathlib import Path
from typing import Dict

from ploto.logger import get_logger


logger = get_logger()


def run_cdo(task: Dict, work_dir: Path, config: Dict):
    input_file = task['input_file']
    output_file = task['output_file']
    params = task['params']

    operator_argument = ','.join(
        [f"{item['old_name']},{item['new_name']}" for item in params])
    input_file_argument = str(Path(work_dir, Path(input_file)))

    output_file_path = Path(work_dir, Path(output_file))
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_file_argument = str(output_file_path)

    command = 'cdo --history --sortname chname,' \
              + operator_argument + ' ' + input_file_argument + ' ' + output_file_argument

    logger.info('run cdo command...')
    logger.info('=> {command}'.format(command=command))
    subprocess.run([command], shell=True, start_new_session=True)
    logger.info('run cdo command...done'.format(command=command))
