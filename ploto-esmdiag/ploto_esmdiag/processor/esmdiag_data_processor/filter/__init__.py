# coding=utf-8
import os
import subprocess
from pathlib import Path

from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
            'action': 'filter',
            'input_file':'',
            'output_file': '',
            'var_name': 'OLR',
            'method': 'butterworth', # or 'lanczos'
            'low_pass': 0.01,
            'high_pass': 0.05,
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()
    method = task['method']

    input_file_path = str(Path(Path(work_dir), task['input_file']))
    output_file_path = str(Path(Path(work_dir), task['output_file']))

    esmdiag_env = os.environ.copy()
    esmdiag_env["ESMDIAG_ROOT"] = config["esmdiag"]["root"]

    logger.info("run ncl script...")

    ncl_script = Path(config["esmdiag"]["root"], 'ncl_scripts', 'filter_{method}.ncl'.format(method=method))
    if not ncl_script.exists():
        logger.error('filter method is not supported: {method}'.format(method=method))

    ncl_command = [
        'ncl -Q '
        '{ncl_script} '
        'var_path=\\"{var_path}\\" '
        'var_name=\\"{var_name}\\" '
        'fca={fca} '
        'fcb={fcb} '
        'out_path=\\"{out_path}\\"'.format(
            var_path=input_file_path,
            var_name=task['var_name'],
            fca=task['low_pass'],
            fcb=task['high_pass'],
            out_path=output_file_path,
            ncl_script=ncl_script)
    ]

    ncl_result = subprocess.run(
        ncl_command,
        env=esmdiag_env,
        # start_new_session=True,
        shell=True,
    )
    logger.info("run ncl script...done")
    return True

