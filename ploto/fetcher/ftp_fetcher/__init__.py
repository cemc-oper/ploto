# coding=utf-8
import ftplib


def download_ftp_data(ftp_file_task, work_dir, config):
    """

    :param ftp_file_task:
        {
            "type": "ftp",
            "host": "ip host",
            "user": "user name",
            "password": "password",
            "directory": "ftp file directory",
            "file_name": "file name"
        },
    :param work_dir:
    :return:
    """
    ftp = ftplib.FTP(ftp_file_task["host"])
    ftp.login(ftp_file_task["user"], ftp_file_task["password"])
    ftp.cwd(ftp_file_task["directory"])
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=ftp_file_task["file_name"]),
        open('{file_path}'.format(file_path=ftp_file_task["file_name"]), 'wb').write
    )
    ftp.quit()


def get_data(task, work_dir, config):
    download_ftp_data(task, work_dir, config)
