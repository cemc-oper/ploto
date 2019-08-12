from flask import request, json, current_app, jsonify

from ploto_server.api import api_v1_app


@api_v1_app.route('/gidat/plot', methods=['POST'])
def receive_plot():
    task_message = None
    if 'task_message' in request.form:
        task_message = json.loads(request.form['task_message'])
    else:
        pass

    if task_message is not None:
        from ploto.scheduler.rabbitmq.producer.producer import send_message
        scheduler_config = current_app.config['server_config']['broker']['scheduler']
        current_app.logger.info('Sending task to scheduler...')
        send_message(task_message, config=scheduler_config)

        return jsonify({
            'status': 'ok',
            'send_count': 1
        })
    else:
        return jsonify({
            'status': 'ok',
            'send_count': 0
        })
