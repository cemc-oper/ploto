# coding=utf-8
"""
cdo processor

Run cdo command.

task schema:
    {
        'type': 'cdo_processor',
        'operator': 'operator',
        ...
    }
"""
from ploto.logger import get_logger


def run_processor(task, work_dir, config):
    logger = get_logger()
    cdo_operator = task['operator']
    if cdo_operator == 'select':
        from ploto.processor.cdo_processor.select import run_cdo
        run_cdo(task, work_dir, config)
    else:
        logger.warn('cod operator is not supported: {cdo_operator}'.format(cdo_operator=cdo_operator))
