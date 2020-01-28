# coding=utf-8
import time

from ploto.scheduler.rabbitmq.producer.producer import send_message


def get_ncl_script():
    return """begin
f = addfile(file_path,"r")

var = f->TMP_P0_L100_GLL0

wks = gsn_open_wks("png", image_path)

res = True
res@tiMainString = "TEMP"
res@cnFillOn = True

plot = gsn_csm_contour_map(wks,var,res)

end
"""


def test_send_task():

    message = {
        'app': 'ploto',
        'type': 'ploto',
        'timestamp': time.time(),
        'data': {
            'data_fetcher': [
                # {
                #     "type": "ftp_fetcher",
                #     "host": "10.28.32.114",
                #     "user": "wangdp",
                #     "password": "perilla",
                #     "directory": "/srv/files/ftp/GRAPES_GFS_ORIG_2017070400",
                #     "file_name": "gmf.gra.2017070400009.grb2"
                # },
                # {
                #     "type": "local_fetcher",
                #     "host": "10.28.32.114",
                #     "user": "wangdp",
                #     "password": "perilla",
                #     "directory": "/srv/files/ftp/GRAPES_GFS_ORIG_2017070400",
                #     "file_name": "gmf.gra.2017070400009.grb2"
                # },
                {
                    'type': 'ploto.fetcher.ddps_fetcher',
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
            ],
            'plotter': {
                'type': 'ncl_plotter',
                'ncl_script_content': get_ncl_script(),
                'image_path': 'image.png',
                'ncl_params': 'file_path=\\"{file_path}\\" image_path=\\"{image_path}\\"'.format(
                    file_path='data_file.grib2',
                    image_path='image.png'
                ),
            }
        }
    }

    send_message(message, config={
        'server': {
            'host': '10.28.32.114',
            'port': 8672
        },
        'routing_keys': {
            'pattern': 'plot.task.*',
            'default': 'plot.task.default'
        },
        'exchange': 'ploto',
        'queue': 'gidat_plot_task_queue'
    })


if __name__ == "__main__":
    test_send_task()
