# coding=utf-8
import json
import ftplib
import uuid
import subprocess
from kafka import KafkaConsumer

import sys
import os
sys.path.append('/home/wangdp/nwpc/gidat/plot/workspace/gidat-plot')


run_base_dir = "/home/wangdp/nwpc/gidat/plot/workspace/run_base"


def download_data(file_path):
    ftp = ftplib.FTP("10.28.32.114")
    ftp.login("wangdp", "perilla")
    ftp.cwd('/srv/files/ftp/GRAPES_GFS_ORIG_2017070400')
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=file_path),
        open('{file_path}'.format(file_path=file_path), 'wb').write)
    ftp.quit()


def save_ncl_script(ncl_script_path, ncl_script):
    with open(ncl_script_path, 'w') as f:
        f.write(ncl_script)


def run_gidat_plot(message):
    print('begin plot...')
    current_directory = os.getcwd()

    print('prepare environment...')
    temp_directory = str(uuid.uuid4())
    os.chdir(run_base_dir)
    work_dir = os.path.join(run_base_dir, temp_directory)
    os.makedirs(work_dir)
    os.chdir(work_dir)

    file_path = message['data']['file_path']
    ncl_script = message['data']['ncl_script']

    param = {
        'file_path': file_path,
        'ncl_script_path': 'draw.ncl'
    }

    print('prepare data...')
    download_data(param['file_path'])
    print('prepare plot script...')
    save_ncl_script(param['ncl_script_path'], ncl_script)

    file_path = param['file_path']
    ncl_script = param['ncl_script_path']

    print('running ncl...')

    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-i', '-c', 'ncl file_path=\\"{file_path}\\" {ncl_script}'.format(
            file_path=file_path,
            ncl_script=ncl_script
        )],
        start_new_session=True
    )

    stdout, stderr = ncl_pipe.communicate()
    ncl_pipe.wait()
    ncl_pipe.terminate()

    print(stdout)
    print(stderr)

    print('running ncl...done')

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
        for consumer_record in consumer:
            print('new message: {offset}'.format(offset=consumer_record.offset))
            message_string = consumer_record.value.decode('utf-8')
            message = json.loads(message_string)
            run_gidat_plot(message)

    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("Warm shutdown...Done")

    consumer.close()


if __name__ == "__main__":
    main()
