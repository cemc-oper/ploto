# coding: utf-8

import logging

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_logger(name='main'):
    logger = logging.getLogger(name)
    logger.setLevel('INFO')
    return logger
