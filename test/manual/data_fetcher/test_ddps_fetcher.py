# coding: utf-8
import os
from gidat_plot.data_fetcher import ddps_fetcher


data_task = {
    'type': 'ddps_fetcher',
    'query_param': {
        "username": "admin",
        "password": "admin",
        "operation": "extractdownload",
        "config": {
            "date": "20140101",
            "groupname": "DYN",
            "expID": "G1600010",
            "time": "1200,12:00",
            "step": "0",
            "levtype": "pl",
            "param": "t",
            "levelist": "850",
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
