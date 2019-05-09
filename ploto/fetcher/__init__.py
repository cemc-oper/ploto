# coding=utf-8
import os
import importlib

from ploto.logger import get_logger
from ploto.fetcher import ftp_fetcher, local_fetcher, ddps_fetcher, edp_fetcher


logger = get_logger()


def run_step(file_steps, work_dir, config):
    os.chdir(work_dir)
    for file_task in file_steps:
        fetcher_type = file_task['type']
        try:
            fetcher = importlib.import_module('ploto.fetcher.{fetcher}'.format(fetcher=fetcher_type))
        except ImportError:
            logger.error("file type not supported: {fetcher}".format(fetcher=fetcher_type))
            continue
        fetcher.get_data(file_task=file_task, work_dir=work_dir, config=config)
