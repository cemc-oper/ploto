# coding=utf-8
from pathlib import Path
import os
import subprocess

from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'esmdiag_data_processor',
            'action': 'lat_avg',
            'start_lat': -10.0,
            'end_lat': 10.0,
            'use_wgt_lat': 'True',
            'input_file': '',
            'var_name': 'U',
            'output_file': ''
            'common_config': {
                'model_info': {
                    'id': "FGOALS-g3",
                    'atm_id': "GAMIL",
                    'ocn_id': "LICOM",
                    'ice_id': "CICE",
                },
                'case_info': {
                    'id': "gamil_wu_run11",
                },
                'date': {
                    'start': "1979-01-01",
                    'end': "1980-12-01"
                }
            }
        }
    :param work_dir:
    :param config:
        {
            'esmdiag': {
                'root': '/home/hujk/ploto/ploto/vendor/esmdiag'
            }
        }
    :return:
    """
    logger = get_logger()

    input_file_path = str(Path(Path(work_dir), task['input_file']))
    output_file_path = str(Path(Path(work_dir), task['output_file']))

    esmdiag_env = os.environ.copy()
    esmdiag_env["ESMDIAG_ROOT"] = config["esmdiag"]["root"]

    logger.info("run ncl script...")

    ncl_script = Path(config["esmdiag"]["root"], 'ncl_scripts', 'lat_avg.ncl')
    if not ncl_script.exists():
        logger.error('ncl script is not found: {path}'.format(path=str(ncl_script)))

    ncl_result = subprocess.run(
        [
            '/bin/bash',
            '-i', '-c',
            'ncl -Q '
            '{ncl_script} '
            'model_id=\\"{model_id}\\" '
            'case_id=\\"{case_id}\\" '
            'start_lat={start_lat} '
            'end_lat={end_lat} '
            'use_wgt_lat={use_wgt_lat} '
            'var_name=\\"{var_name}\\" '
            'var_path=\\"{var_path}\\" '
            'out_path=\\"{out_path}\\"'.format(
                model_id=task['common_config']['model_info']['atm_id'],
                case_id=task['common_config']['case_info']['id'],
                start_lat=task['start_lat'],
                end_lat=task['end_lat'],
                use_wgt_lat=task['use_wgt_lat'],
                var_path=input_file_path,
                var_name=task['var_name'],
                out_path=output_file_path,
                ncl_script=ncl_script)
        ],
        env=esmdiag_env,
        start_new_session=True
    )
    logger.info("run ncl script...done")
    return True
