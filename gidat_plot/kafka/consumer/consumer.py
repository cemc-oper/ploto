# coding=utf-8
import json
import sys
import os

from kafka import KafkaConsumer
import click
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../../"))
from gidat_plot.run import run_gidat_plot


@click.command()
@click.option("-c", "--config-file", help="config file path")
def cli(config_file):
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
    cli()
