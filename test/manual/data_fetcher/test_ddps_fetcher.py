# coding: utf-8
import os
from gidat_plot.data_fetcher import ddps_fetcher


data_task = {
    'type': 'ddps',
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
    }
}


work_dir = "/home/wangdp/nwpc/gidat/plot/workspace/temp"


ddps_fetcher.get_data(data_task, work_dir)
