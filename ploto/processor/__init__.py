# coding=utf-8
import importlib

from ploto.logger import get_logger


logger = get_logger()


def run_step(processor_steps, work_dir, config):
    for task in processor_steps:
        processor_type = task['type']
        try:
            processor_module = importlib.import_module('ploto.processor/{processor_type}'.format(
                processor_type=processor_type
            ))
        except ImportError:
            logger.error("processor type not supported: {processor_type}".format(
                processor_type=processor_type))
            continue
        processor_module.run_processor(task, work_dir, config)
