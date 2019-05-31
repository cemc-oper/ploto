# coding=utf-8
import json
import threading
import time

import click
import yaml
import pika

from ploto.run import run_ploto
from ploto.logger import get_logger


def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
        return config


def process_message(message, config):
    run_ploto(message, config)


@click.command()
@click.option("-c", "--config-file", help="config file path")
def cli(config_file):
    logger = get_logger()
    config = load_config(config_file)

    rabbitmq_config = config['rabbitmq']
    exchange_name = rabbitmq_config['exchange']
    queue_name = rabbitmq_config['queue']

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=rabbitmq_config['server']['host'],
            port=rabbitmq_config['server']['port']
        )
    )

    channel = connection.channel()

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
        routing_key=rabbitmq_config['routing_keys']['pattern']
    )

    def consume_message(ch, method, properties, body):
        logger.info('receive new message')
        message_string = body.decode('utf-8')
        message = json.loads(message_string)
        message_thread = threading.Thread(target=process_message, args=(message, config))
        message_thread.start()

        while message_thread.is_alive():
            time.sleep(10)
            connection.process_data_events()
            # logger.info("waiting for message thread...")
        logger.info("message thread done")

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue_name,
        consume_message,
        auto_ack=True
    )

    try:
        logger.info("starting receiving message...")
        channel.start_consuming()
    except KeyboardInterrupt as e:
        logger.info("Shutdown by KeyboardInterrupt")
        logger.info(e)
    finally:
        logger.info("Warm shutdown...")
        channel.stop_consuming()
        connection.close()
        logger.info("Warm shutdown...Done")


if __name__ == "__main__":
    cli()
