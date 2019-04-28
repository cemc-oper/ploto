# coding=utf-8
import os
from ploto.logger import get_logger
from ploto.fetcher import ftp_fetcher, local_fetcher, ddps_fetcher, edp_fetcher


data_fetcher_mapper = {
    'ftp_fetcher': ftp_fetcher,
    'local_fetcher': local_fetcher,
    'ddps_fetcher': ddps_fetcher,
    'edp_fetcher': edp_fetcher,
}


logger = get_logger()


def run_fetcher(files, work_dir, config):
    os.chdir(work_dir)
    for file_task in files:
        file_type = file_task['type']
        fetcher = data_fetcher_mapper.get(file_type, None)

        if fetcher:
            fetcher.get_data(file_task, work_dir, config)
        else:
            logger.warn("file type not supported: {file_type}".format(file_type=file_type))
