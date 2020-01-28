# coding=utf-8
import importlib

from ploto.logger import get_logger


logger = get_logger()


def run_step(step, work_dir, config):
    processor_type = step['type']
    try:
        processor_module = importlib.import_module(
            '{processor_type}'.format(processor_type=processor_type)
        )
    except ImportError:
        logger.error("processor type not supported: {processor_type}".format(
            processor_type=processor_type))
        return
    processor_module.run_processor(task=step, work_dir=work_dir, config=config)
