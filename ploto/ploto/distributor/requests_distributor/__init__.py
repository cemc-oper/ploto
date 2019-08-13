# coding=utf-8
"""
requests distributor

Send messages using requests.

task schema:
    {
        'type': 'requests_distributor',
        'url: url, # optional, must have at least one.
        'requests': [
            {
                'method': "POST"/"GET"
                'url': url # optional,
                'data': {
                    key: value
                }
            }
        ]
    }
"""
import requests

from ploto.logger import get_logger


def run_distributor(task: dict, work_dir, config):
    logger = get_logger()
    url = task.get('url', None)

    for request_task in task['requests']:
        method = task.get('method', 'POST')
        request_task_url = request_task.get('url', url)
        if request_task_url is None:
            logger.warnning('url must be sent')
            continue
        data = request_task['data']
        logger.info('sending request...')
        logger.info('   => url: {url}'.format(url=request_task_url))
        result = requests.request(method, request_task_url, data=data, timeout=10)
        logger.info('   => result: {result}'.format(result=result.text))
        logger.info('sending request...done')

    return True
