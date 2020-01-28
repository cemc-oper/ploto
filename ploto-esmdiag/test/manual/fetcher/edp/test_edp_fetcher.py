# coding: utf-8
from ploto_esmdiag.fetcher import edp_fetcher


def test_edp_fetcher():
    data_task = {
        'type': 'ploto_esmdiag.fetcher.edp_fetcher',
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

    edp_config = {
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/pyProject/"
        }
    }

    edp_fetcher.get_data(
        data_task,
        work_dir,
        config=edp_config
    )


if __name__ == "__main__":
    test_edp_fetcher()
