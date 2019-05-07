# coding: utf-8
from flask import request, json, current_app, jsonify

from ploto_server.api import api_v1_app

from ploto_server.common.esmdiag import generate_metric_tasks


@api_v1_app.route('/esmdiag/plot', methods=['POST'])
def receive_esmdiag_plot():
    """

    POST DATA
    task
        {
            model_info: {
                id: "FGOALS-g3",
                atm_id: "GAMIL",
                ocn_id: "LICOM",
                ice_id: "CICE",
            },
            case_info: {
                id: "piControl-bugfix-licom-80368d",
            },
            date: {
                start: "0030-01-01",
                end: "0060-12-31"
            }
            metrics: [
                {
                    name: 'climo',
                    figures: [
                        { name: 'precip'},
                        { name: 'swcf'},
                    ]
                }
            ]
        }
    """
    task_message = None
    if 'task_message' in request.form:
        task_message = json.loads(request.form['task_message'])
    else:
        pass

    common_config = {
        'model_info': task_message['model_info'],
        'case_info': task_message['case_info'],
        'date': task_message['date'],
    }

    metrics_config = task_message['metrics_config']

    all_tasks = []

    for metric_config in metrics_config:
        tasks = generate_metric_tasks(metric_config, common_config)
        all_tasks.extend(tasks)

    for task in all_tasks:
        from ploto.scheduler.rabbitmq.producer.producer import send_message
        scheduler_config = current_app.config['BROKER_CONFIG']['scheduler']
        current_app.logger.info('Sending task to scheduler...')
        message = {
            'data': task
        }
        send_message(message, config=scheduler_config)

    return jsonify({
        'status': 'ok',
        'send_count': len(all_tasks)
    })
