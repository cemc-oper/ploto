# coding=utf-8
from pathlib import Path

from ploto.logger import get_logger


def run_processor(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
            'action': 'anomaly',
            'input_file':'',
            'output_file': '',
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()

    input_file_path = str(Path(Path(work_dir), task['input_file']))
    output_file_path = str(Path(Path(work_dir), task['output_file']))

    from ploto.processor.cdo_processor.general import run_cdo
    step1_task = {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'general',
        'params': [
            'timmean',
            input_file_path,
            output_file_path + ".step1"
        ],
    }
    run_cdo(step1_task, work_dir, config)
    step2_task = {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'general',
        'params': [
            'sub',
            input_file_path,
            output_file_path + ".step1",
            output_file_path
        ],
    }
    run_cdo(step2_task, work_dir, config)

    Path(output_file_path + ".step1").unlink()

    return True
