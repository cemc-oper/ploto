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


@api_v1_app.route('/gidat/plot-metgui', methods=['POST'])
def receive_plot_metgui():
    plot_task = None
    if 'plot_task' in request.form:
        plot_task = json.loads(request.form['plot_task'])
    else:
        return jsonify({
            'status': 'ok',
            'send_count': 0
        })

    if plot_task is not None:
        from gidat_server.common.metgui import create_message_from_plot_task
        message = create_message_from_plot_task(plot_task)

        # print(json.dumps(message, indent=2))

        from gidat_plot.scheduler.rabbitmq.producer.producer import send_message
        scheduler_config = current_app.config['BROKER_CONFIG']['scheduler']
        current_app.logger.info('Sending task to scheduler...')
        send_message(message, config=scheduler_config)

        return jsonify({
            'status': 'ok',
            'send_count': 1
        })
    else:
        return jsonify({
            'status': 'ok',
            'send_count': 0
        })
