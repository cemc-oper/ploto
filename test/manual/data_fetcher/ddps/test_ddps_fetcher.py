# coding: utf-8
import os
from ploto.data_fetcher import ddps_fetcher


def main():
    data_task = {
        'type': 'ddps_fetcher',
        'query_param': {
            "username": "admin",
            "password": "admin",
            "operation": "extractdownload",
            "config": {
                "groupname": "DYN",
                "expID": "G1600010",
                "date": "20140101",
                "time": "1200,12:00",
                "step": "0",
                "levtype": "2",
                "param": "hcc",
                "levelist": "0",
                "savePath": "./ddps"
            }
        },
        'file_name': 'data_file.grib2'
    }

    work_dir = "/space/windroc/workspace/plot/playground/temp"

    ddps_fetcher.get_data(data_task, work_dir, config={
        'ddps_fetcher': {
            'bsc_command': "/space/project/BSC/bsc/bin/bsc"
        }
    })


if __name__ == "__main__":
    main()
