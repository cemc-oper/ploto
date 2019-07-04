# coding=utf-8
"""
convert processor

Run convert command.

task schema:
    {
        'type': 'convert_processor',
        'operator': 'general',
        'params' :[
            '-density 300',
            '-set filename.f "%t"',
            '*.pdf',
            '%[filename.f].png'
        ]
    }
"""
from pathlib import Path
import subprocess

from ploto.logger import get_logger


def run_processor(task, work_dir, config):
    logger = get_logger()
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

    command = 'convert ' \
              + operator_argument

    logger.info('run convert command...')
    logger.info('=> {command}'.format(command=command))
    subprocess.run([command], shell=True, start_new_session=True)
    logger.info('run convert command...done'.format(command=command))
    return True
