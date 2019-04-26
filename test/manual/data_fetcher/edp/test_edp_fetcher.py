# coding: utf-8
from ploto.data_fetcher import edp_fetcher


def main():
    data_task = {
        'type': 'edp_fetcher',
        'query_param': {
            'type': 'nc',
            'output_dir': './data',
            'file_prefix': 'GAMIL.gamil_wu_run11',
            'date_range': ['19810101', '19820101'],
            'field_names': [
                'PRECT',
                'PRECC',
                'PRECL',
                'PS'
            ],
            'datedif': 'h0'
        }
    }

    work_dir = "/home/hujk/clusterfs/wangdp/temp"

    edp_fetcher.get_data(data_task, work_dir, config={
        'edp_fetcher': {
            'edp_script': "/home/hujk/ploto/script/edp.py"
        }
    })


if __name__ == "__main__":
    main()
