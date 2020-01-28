# coding: utf-8
import requests
import json


def test_api_climo_prod():
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
                    {'name': 'precip'},
                    {'name': 'swcf'},
                    {'name': 'lwcf'},
                    {'name': 'zonal_mean'},
                ]
            }
        ]
    }

    result = requests.post("http://localhost:8060/api/v1/esmdiag/plot", data={
        'task_message': json.dumps(task_message)
    })


if __name__ == "__main__":
    test_api_climo_prod()
