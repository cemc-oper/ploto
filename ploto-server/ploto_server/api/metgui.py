from flask import request, json, jsonify, current_app

from ploto_server.api import api_v1_app


@api_v1_app.route('/gidat/plot-metgui', methods=['POST'])
def receive_plot_metgui():
    plot_task = None
    if 'plot_task' in request.form:
        plot_task = json.loads(request.form['plot_task'])
    elif 'plot_task' in request.json:
        plot_task = json.loads(request.json['plot_task'])
    else:
        return jsonify({
            'status': 'ok',
            'send_count': 0
        })

    if plot_task is not None:
        from ploto_server.common.metgui import create_message_from_plot_task
        message = create_message_from_plot_task(plot_task)

        # print(json.dumps(message, indent=2))

        from ploto.scheduler.rabbitmq.producer.producer import send_message
        scheduler_config = current_app.config['server_config']['broker']['scheduler']
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