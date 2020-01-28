# coding=utf-8
"""
Run cdo select operator.

task schema:
    {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'select',
        'params': {
            'name': 'PS',
            'startdate': '1981-01-01',
            'enddate': '1982-01-01',
        },
        'input_files': [
            './data/GAMIL.gamil_wu_run11*.nc',
        ],
        'output_file': './temp/GAMIL.gamil_wu_run11.PS.monthly.1981-01-01:1981-12-31.nc',
    }
"""
import subprocess
from pathlib import Path
from ploto.logger import get_logger

logger = get_logger()


def run_cdo(task, work_dir, config):
    input_files = task['input_files']
    output_file = task['output_file']
    select_params = task['params']

    select_argument = ','.join(
        ['{key}={value}'.format(key=key, value=select_params[key]) for key in select_params])
    input_files_argument = ' '.join([str(Path(work_dir, Path(item))) for item in input_files])

    output_file_path = Path(work_dir, Path(output_file))
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    output_file_argument = str(output_file_path)

    command = 'cdo --history --sortname select,' \
              + select_argument + ' ' + input_files_argument + ' ' + output_file_argument

    logger.info('run cdo command...')
    logger.info('=> {command}'.format(command=command))
    subprocess.run([command], shell=True, start_new_session=True)
    logger.info('run cdo command...done'.format(command=command))
