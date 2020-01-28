# coding=utf-8
import time
import json
import os
import asyncio
import warnings

from aiokafka import AIOKafkaProducer


def test_local_file_and_ncldraw():
    warnings.warn("ncldraw is no longer used", DeprecationWarning)
    loop = asyncio.get_event_loop()

    async def send_one():
        producer = AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=['{kafka_host}:{kafka_port}'.format(
                kafka_host='localhost',
                kafka_port=9092)
            ]
        )
        await producer.start()

        task_file_path = os.path.join(os.path.dirname(__file__), "task.xml")

        kafka_topic = "gidat-plot"
        message = {
            'app': 'gidat-plot',
            'type': 'gidat-plot',
            'timestamp': time.time(),
            'data': {
                'data_fetcher': [
                    # {
                    #     "type": "ftp_fetcher",
                    #     "host": "10.28.32.114",
                    #     "user": "user",
                    #     "password": "password",
                    #     "directory": "/srv/files/ftp/GRAPES_GFS_ORIG_2017070400",
                    #     "file_name": "gmf.gra.2017070400009.grb2"
                    # },
                    {
                        "type": "local_fetcher",
                        "directory": "/space/windroc/workspace/plot/playground/test_case_1",
                        "file_name": "data.grb2"
                    },
                    # {
                    #     'type': 'ddps_fetcher',
                    #     'query_param': {
                    #         "username": "admin",
                    #         "password": "admin",
                    #         "operation": "extractdownload",
                    #         "config": {
                    #             "date": "20140101",
                    #             "groupname": "DYN",
                    #             "expID": "G1600010",
                    #             "time": "1200,12:00",
                    #             "step": "0",
                    #             "levtype": "pl",
                    #             "param": "t",
                    #             "levelist": "850",
                    #             "savePath": "./ddps"
                    #         }
                    #     },
                    #     'file_name': 'data_file.grib2'
                    # }
                ],
                'plotter': {
                    'type': 'ncldraw_plotter',
                    'task_files': [
                        {
                            'file_path': task_file_path,
                            'file_content': open(task_file_path).read()
                        }
                    ],
                    'time_level': '2017071400084',
                    'image_path': 'image.png',
                },
                'post_processor': [
                    {
                        'type': 'copy_file_processor',
                        'files': [
                            {
                                'from': 'image.png',
                                'to': 'image_output.png'
                            }
                        ]
                    }
                ]
            }
        }

        message_string = json.dumps(message)
        print(message_string)

        try:
            record_metadata = await producer.send_and_wait(kafka_topic, message_string.encode('utf-8'))

            print(record_metadata.topic)
            print(record_metadata.partition)
            print(record_metadata.offset)
        finally:
            await producer.stop()

        return {'status': 'ok'}

    loop.run_until_complete(send_one())


if __name__ == "__main__":
    test_local_file_and_ncldraw()
