# coding=utf-8
import os
import importlib

from ploto.logger import get_logger
from ploto.fetcher import ftp_fetcher, local_fetcher, edp_fetcher

logger = get_logger()


def run_step(step, work_dir, config):
    os.chdir(work_dir)
    fetcher_type = step['type']
    try:
        fetcher = importlib.import_module('{fetcher}'.format(fetcher=fetcher_type))
    except ImportError:
        logger.error("file type not supported: {fetcher}".format(fetcher=fetcher_type))
        return
    fetcher.get_data(task=step, work_dir=work_dir, config=config)
