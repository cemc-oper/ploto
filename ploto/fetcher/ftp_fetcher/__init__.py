import ftplib
from typing import Dict
from pathlib import Path


def download_ftp_data(ftp_file_task: Dict, work_dir: Path, config: Dict):
    """

    Parameters
    ----------
    ftp_file_task

        {
            "type": "ploto.fetcher.ftp_fetcher",
            "host": "ip host",
            "user": "user name",
            "password": "password",
            "directory": "ftp file directory",
            "file_name": "file name"
        }

    work_dir
    config

    Returns
    -------

    """
    ftp = ftplib.FTP(ftp_file_task["host"])
    ftp.login(ftp_file_task["user"], ftp_file_task["password"])
    ftp.cwd(ftp_file_task["directory"])
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=ftp_file_task["file_name"]),
        open('{file_path}'.format(file_path=ftp_file_task["file_name"]), 'wb').write
    )
    ftp.quit()


def get_data(task: Dict, work_dir: Path, config: Dict):
    download_ftp_data(task, work_dir, config)
