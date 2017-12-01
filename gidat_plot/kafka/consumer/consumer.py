# coding=utf-8
import json
import uuid
from kafka import KafkaConsumer

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../../"))

from gidat_plot.plotter.ncl_plotter import ncl_script_util
from gidat_plot.data_fetcher import ftp_fetcher, local_fetcher


run_base_dir = "/home/wangdp/nwpc/gidat/plot/workspace/run_base"


def prepare_environment():
    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    os.makedirs(work_dir)
    os.chdir(work_dir)
    return work_dir


def prepare_data(files, work_dir):
    os.chdir(work_dir)
    for file_task in files:
        file_type = file_task['type']
        if file_type == 'ftp':
            ftp_fetcher.get_data(file_task, work_dir)
        elif file_type == 'local':
            local_fetcher.get_data(file_task, work_dir)
        else:
            print("file type not supported:", file_type)


def draw_plot(plotter_config, work_dir):
    if plotter_config['type'] == 'ncl_plotter':
        ncl_script_util.run_plotter(plotter_config, work_dir)
    else:
        print("plotter type is not supported:", plotter_config['type'])


def clear_environment(work_dir):
    pass


def run_gidat_plot(message):
    print('begin plot...')
    current_directory = os.getcwd()

    print('prepare environment...')
    work_dir = prepare_environment()

    print('prepare data...')
    files = message['data']['files']
    prepare_data(files, work_dir)

    print('drawing plot...')
    draw_plot(message['data']['plotter'], work_dir)

    print('clearing environment...')
    clear_environment(work_dir)

    os.chdir(current_directory)
    print('end plot')


def main():
    kafka_topic = 'gidat_plot'
    kafka_group = 'gidat_plot_group'

    consumer = KafkaConsumer(
        kafka_topic,
        group_id=kafka_group,
        bootstrap_servers=[
            '{kafka_host}:{kafka_port}'.format(
                kafka_host='10.28.32.114',
                kafka_port=9092)
        ]
    )
    consumer.max_buffer_size = 1000000

    try:
        print("starting receiving message...")
        for consumer_record in consumer:
            print('new message: {offset}'.format(offset=consumer_record.offset))
            message_string = consumer_record.value.decode('utf-8')
            message = json.loads(message_string)
            run_gidat_plot(message)

    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("Warm shutdown...")
        consumer.close()
        print("Warm shutdown...Done")


if __name__ == "__main__":
    main()
