# coding=utf-8
"""
cdo chname

task schema:
    {
        'type': 'cdo_processor',
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
from ploto.logger import get_logger

logger = get_logger()


def run_cdo(task, work_dir, config):
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
                logger.error("param type is not support: {param_type}".format(param_type=param_type))
                return

    operator_argument = ' '.join([item for item in compiled_params])

    command = 'cdo --history ' \
              + operator_argument

    logger.info('run cdo command...')
    logger.info('=> {command}'.format(command=command))
    subprocess.run([command], shell=True, start_new_session=True)
    logger.info('run cdo command...done'.format(command=command))