# coding: utf-8
from flask import request, json, current_app, jsonify

from ploto_server.api import api_v1_app

from ploto_server.common.esmdiag import generate_metric_tasks


@api_v1_app.route('/esmdiag/plot', methods=['POST'])
def receive_esmdiag_plot():
    """

    POST DATA
    task_message
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

    model_info: 模式信息
        id: 模式id
        atm_id: 大气分量模式id
        ocn_id: 海洋分量模式id
        ice_id: 海冰分量模式id
    case_info: 试验信息
        id: 试验id
    date: 时间范围
        start: 起始时间，YYYY-MM-DD
        end: 终止时间，YYYY-MM-DD
    metrics: 数组，诊断方法列表，每个项目包含字段名
        name: 诊断类型，[climo, mjo]
        figures: 子类型列表，每个项目包含字段名
            name: 子类型名，例如
                climo包括：
                    energy_balance
                    ice_area
                    lwcf
                    precip
                    radition_energy_budget
                    swcf
                    zonal_mean
                mjo包括：
                    combined_eof
                    lag
                    mean_state
                    variance_ratio
                    wavenum_freq_spectra

    返回值：
        {
            'status': 'ok',
            'send_count': task_count 发送的任务数量
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
