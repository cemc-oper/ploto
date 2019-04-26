# coding=utf-8
from ploto.logger import get_logger


def run_pre_processor(task, work_dir, config):
    logger = get_logger()
    logger.info("task type not supported: {type}".format(type=task['type']))
