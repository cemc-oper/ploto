"""
cdo

task schema:
    {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'general',
        'params': [
            'sub',
            {
                'type': 'file',
                'value': 'GAMIL.gamil_wu_run11.OLR.daily.1979-01-01:1980-12-31.nc',
            },
            '-timmean',
            {
                'type': 'file',
                'value': 'GAMIL.gamil_wu_run11.OLR.daily.1979-01-01:1980-12-31.nc',
            },
        ],
}
"""
import subprocess
from pathlib import Path
from typing import Dict


from ploto.logger import get_logger

logger = get_logger()


def run_cdo(task: Dict, work_dir: Path, config: Dict):
    params = task['params']

    compiled_params = []
    for item in params:
        if isinstance(item, str):
            compiled_params.append(item)
        else:
            param_type = item['type']
            if param_type == 'file':
                item_string = str(Path(work_dir, Path(item['value'])))
                compiled_params.append(item_string)
            else:
                logger.error(f"param type is not support: {param_type}")
                return

    operator_argument = ' '.join([item for item in compiled_params])

    command = 'cdo --history ' \
              + operator_argument

    logger.info('run cdo command...')
    logger.info(f'=> {command}')
    subprocess.run([command], shell=True, start_new_session=True)
    logger.info('run cdo command...done')
