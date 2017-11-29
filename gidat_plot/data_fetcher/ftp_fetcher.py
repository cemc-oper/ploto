# coding=utf-8
import ftplib


def download_ftp_data(ftp_file_task):
    ftp = ftplib.FTP(ftp_file_task["host"])
    ftp.login(ftp_file_task["user"], ftp_file_task["password"])
    ftp.cwd(ftp_file_task["directory"])
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=ftp_file_task["file_name"]),
        open('{file_path}'.format(file_path=ftp_file_task["file_name"]), 'wb').write
    )
    ftp.quit()