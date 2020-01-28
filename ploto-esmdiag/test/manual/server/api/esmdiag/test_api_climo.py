# coding: utf-8
import requests
import json
import uuid


def test_api_climo():
    task_message = {
        'model_info': {
            'id': "FGOALS-g3",
            'atm_id': "GAMIL",
            'ocn_id': "LICOM",
            'ice_id': "CICE",
        },
        'case_info': {
            'id': "gamil_wu_run11",
        },
        'date': {
            'start': "1981-01-01",
            'end': "1981-12-01"
        },
        'metrics_config': [
            {
                'name': 'climo',
                'figures': [
                    {'name': 'precip', 'task_id': str(uuid.uuid4())},
                    {'name': 'swcf', 'task_id': str(uuid.uuid4())},
                    {'name': 'lwcf', 'task_id': str(uuid.uuid4())},
                    {'name': 'zonal_mean', 'task_id': str(uuid.uuid4())},
                ]
            }
        ]
    }

    url = "http://localhost:8085/api/v1/esmdiag/plot"
    result = requests.post(url, data={
        'task_message': json.dumps(task_message)
    })


if __name__ == "__main__":
    test_api_climo()
