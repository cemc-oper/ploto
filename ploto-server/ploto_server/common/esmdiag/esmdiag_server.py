# coding: utf-8
from enum import Enum


class TaskStatus(Enum):
    Queued = 1
    Active = 2
    Complete = 3
    Aborted = 4


def get_send_status_steps(status: TaskStatus, figure_config, common_config, server_config):
    """
    :param status: figure task status
    :param figure_config:
        {
            name: '...',
            task_id: 'task_id'
        }
    :param common_config:
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
        }
    :param server_config:
        {
            'esmdiag': {
                'web: {
                    'url': url,
                    'api': {
                        'task_status': task_status api
                    }
                }
            }
        }
    :return:
    """
    esmdiag_web_config = server_config['esmdiag']['web']
    steps = [
        {
            'step_type': 'distributor',
            'type': 'ploto.distributor.requests_distributor',
            'url': "{base_url}{api_path}".format(
                base_url=esmdiag_web_config['url'],
                api_path=esmdiag_web_config['api']['task_status']),
            'requests': [
                {
                    'method': 'POST',
                    'data': {
                        'task_id': figure_config['task_id'],
                        'status': status.value,
                        'message': '',
                        'user_id': 'default',
                        'token': '',
                    }
                }
            ]
        }
    ]
    return steps


def get_local_distribution_steps(figure_config, common_config, server_config):
    """
    copy all png files on work dir to esmdiag's web plot base dir.

    :param figure_config:
        {
            name: '...',
            task_id: 'task_id'
        }
    :param common_config:
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
        }
    :param server_config:
        {
            'esmdiag': {
                'web: {
                    'plot_base_dir': 'plot base dir'
                }
            }
        }
    :return:
    """
    esmdiag_web_config = server_config['esmdiag']['web']
    steps = [
        {
            'step_type': 'distributor',
            'type': 'ploto.distributor.local_distributor',
            'items': [
                {
                    'from': './*.png',
                    'to': "{plot_base_dir}/{task_id}".format(
                        plot_base_dir=esmdiag_web_config['plot_base_dir'],
                        task_id=figure_config['task_id']),
                }
            ]
        }
    ]
    return steps
