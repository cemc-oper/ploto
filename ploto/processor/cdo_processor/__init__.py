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
import importlib

from ploto.logger import get_logger


def run_processor(task, work_dir, config):
    logger = get_logger()
    cdo_operator = task['operator']
    try:
        operator_module = importlib.import_module(
            ".{operator}".format(operator=cdo_operator), __package__)
    except ImportError:
        logger.error("cdo operator not supported: {operator}".format(
            operator=cdo_operator))
        return False
    operator_module.run_cdo(task, work_dir, config)
    return True
