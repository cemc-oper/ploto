# coding=utf-8
import json
import sys
import os

from kafka import KafkaConsumer
import click
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../../"))
from gidat_plot.run import run_gidat_plot


def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)
        return config


@click.command()
@click.option("-c", "--config-file", help="config file path")
def cli(config_file):

    config = load_config(config_file)

    kafka_config = config['kafka']
    kafka_topic = kafka_config['topic']
    kafka_group = kafka_config['group']

    consumer = KafkaConsumer(
        kafka_topic,
        group_id=kafka_group,
        bootstrap_servers=[
            '{kafka_host}:{kafka_port}'.format(
                kafka_host=kafka_config['host'],
                kafka_port=kafka_config['port'])
        ]
    )
    consumer.max_buffer_size = 1000000

    try:
        print("starting receiving message...")
        for consumer_record in consumer:
            print('new message: {offset}'.format(offset=consumer_record.offset))
            message_string = consumer_record.value.decode('utf-8')
            message = json.loads(message_string)
            run_gidat_plot(message, config)

    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("Warm shutdown...")
        consumer.close()
        print("Warm shutdown...Done")


if __name__ == "__main__":
    cli()
