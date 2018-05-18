# coding=utf-8
import time
import json

import click
import pika


def send_message(message: dict, config: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=config['server']['host'],
            port=config['server']['port']
        )
    )

    channel = connection.channel()

    exchange_name = config['exchange']
    queue_name = config['queue']

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type="topic"
    )

    channel.queue_declare(
        queue=queue_name
    )

    channel.queue_bind(
        exchange=exchange_name,
        queue=queue_name,
        routing_key=config['routing_keys']['pattern']
    )

    message_string = json.dumps(message)
    print(message_string)
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=config['routing_keys']['default'],
        body=message_string.encode('utf-8'))

    connection.close()

    return {'status': 'ok'}


if __name__ == "__main__":
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

    message = {
        'app': 'gidat_plot',
        'type': 'gidat_plot',
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
        'exchange': 'gidat_plot',
        'queue': 'gidat_plot_task_queue'
    })
