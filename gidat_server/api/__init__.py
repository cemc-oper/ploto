# coding=utf-8
from flask import Blueprint, request, current_app, json, jsonify

api_v1_app = Blueprint('api_v1_app', __name__, template_folder='template')


@api_v1_app.route('/gidat/plot', methods=['POST'])
def receive_plot():
    task_message = None
    if 'task_message' in request.form:
        task_message = json.loads(request.form['task_message'])
    else:
        pass

    if task_message is not None:
        from gidat_plot.scheduler.rabbitmq.producer.producer import send_message
        scheduler_config = current_app.config['BROKER_CONFIG']['scheduler']
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
