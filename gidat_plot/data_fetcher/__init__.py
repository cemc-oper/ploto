# coding=utf-8
import os


def prepare_data(files, work_dir, config):
    from gidat_plot.data_fetcher import ftp_fetcher, local_fetcher, ddps_fetcher
    data_fetcher_mapper = {
        'ftp_fetcher': ftp_fetcher,
        'local_fetcher': local_fetcher,
        'ddps_fetcher': ddps_fetcher
    }
    os.chdir(work_dir)
    for file_task in files:
        file_type = file_task['type']
        fetcher = data_fetcher_mapper.get(file_type, None)

        if fetcher:
            fetcher.get_data(file_task, work_dir, config)
        else:
            print("file type not supported:", file_type)
