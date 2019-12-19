# coding: utf-8
import datetime


def generate_fetcher_params(drag_run_config: dict, fields: list) -> dict:
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    start_date = datetime.datetime.strptime(common_config['date']['start'], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config['date']['end'], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    file_prefix = '{atm_id}.{case_id}'.format(
        atm_id=common_config['model_info']['atm_id'],
        case_id=common_config['case_info']['id'],
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    task_config = {
        'step_type': 'fetcher',
        'common': common_config,
        'type': 'edp_fetcher',
        'query_param': {
            'type': 'nc',
            'output_dir': './data',
            'file_prefix': step1_file_prefix,
            'date_range': date_range,
            'field_names': fields,
            'datedif': 'h0'
        },
    }
    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_cdo_select_params(drag_run_config: dict, field: str) -> dict:
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    file_prefix = '{atm_id}.{case_id}'.format(
        atm_id=common_config['model_info']['atm_id'],
        case_id=common_config['case_info']['id']
    )

    step1_file_prefix = '{file_prefix}.step1'.format(
        file_prefix=file_prefix
    )

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config['date']['start'],
        end_date=common_config['date']['end'],
    )
    output_file_pattern = "{file_prefix}.{name}.monthly.{time_range}.nc"

    task_config = {
        'step_type': 'processor',
        'type': 'cdo_processor',
        'operator': 'select',
        'params': {
            'name': field,
            'startdate': common_config['date']['start'],
            'enddate': common_config['date']['end']
        },
        'input_files': [
            './data/{step1_file_prefix}.*.nc'.format(step1_file_prefix=step1_file_prefix)
        ],
        'output_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name=field,
        ),
    }
    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }
