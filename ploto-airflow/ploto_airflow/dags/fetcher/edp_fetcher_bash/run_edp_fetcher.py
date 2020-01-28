# coding: utf-8
"""python command line tool for bash operator.
"""
import json

import click

from ploto.fetcher import edp_fetcher


@click.command()
@click.option("--step-config", help="step config")
def run_edp_fetcher_step(step_config):
    step_config = json.loads(step_config)
    # task = drag_run_config["task"]
    work_dir = step_config["work_dir"]
    # config = drag_run_config["config"]

    task = {
        'type': 'ploto.fetcher.edp_fetcher',
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

    # work_dir = "/home/hujk/clusterfs/wangdp/temp"

    config = {
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/pyProject/"
        }
    }

    edp_fetcher.get_data(
        task,
        work_dir,
        config=config
    )


if __name__ == "__main__":
    run_edp_fetcher_step()
