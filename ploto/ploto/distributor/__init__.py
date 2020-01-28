# coding=utf-8
import importlib

from ploto.logger import get_logger


logger = get_logger()


def run_step(step, work_dir, config):
    distributor_type = step['type']
    try:
        distributor_module = importlib.import_module(
            '{distributor_type}'.format(distributor_type=distributor_type)
        )
    except ImportError:
        logger.error("distributor type not supported: {distributor_type}".format(
            distributor_type=distributor_type))
        return
    distributor_module.run_distributor(task=step, work_dir=work_dir, config=config)
