# coding=utf-8
import json
import sys
import os
import asyncio
import threading
import time

from aiokafka import AIOKafkaConsumer
import click
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../../"))
from gidat_plot.run import run_gidat_plot
from gidat_plot.logger import get_logger


def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.load(f)
        return config


def process_message(message, config):
    # run_gidat_plot(message, config)
    time.sleep(10)


@click.command()
@click.option("-c", "--config-file", help="config file path")
def cli(config_file):
    logger = get_logger()
    config = load_config(config_file)

    kafka_config = config['kafka']
    kafka_topic = kafka_config['topic']
    kafka_group = kafka_config['group']

    loop = asyncio.get_event_loop()

    async def consume():
        consumer = AIOKafkaConsumer(
            kafka_topic,
            loop=loop,
            bootstrap_servers=[
                '{kafka_host}:{kafka_port}'.format(
                    kafka_host=kafka_config['host'],
                    kafka_port=kafka_config['port'])
            ],
            group_id=kafka_group
        )

        await consumer.start()
        try:
            logger.info("starting receiving message...")
            async for consumer_record in consumer:
                consumer.commit()
                logger.info('receive new message: {offset}'.format(offset=consumer_record.offset))
                message_string = consumer_record.value.decode('utf-8')
                message = json.loads(message_string)
                message_thread = threading.Thread(target=process_message, args=(message, config))
                message_thread.start()

                while message_thread.is_alive():
                    await asyncio.sleep(10)
                    logger.info("waiting for message thread...")
                logger.info("message thread done")

        except KeyboardInterrupt as e:
            logger.info(e)
        finally:
            logger.info("Warm shutdown...")
            await consumer.stop()
            logger.info("Warm shutdown...Done")

    loop.run_until_complete(consume())


if __name__ == "__main__":
    cli()
