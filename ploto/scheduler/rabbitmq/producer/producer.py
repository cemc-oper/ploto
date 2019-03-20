# coding=utf-8
import time
import json

import click
import pika
import yaml


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
    # print(message_string)
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=config['routing_keys']['default'],
        body=message_string.encode('utf-8'))

    connection.close()

    return {'status': 'ok'}


@click.command()
@click.option("-c", "--config-file", help="config file path")
def cli(config_file):
    pass


if __name__ == "__main__":
    cli()
