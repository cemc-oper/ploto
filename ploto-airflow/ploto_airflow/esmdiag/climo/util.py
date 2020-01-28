# coding: utf-8
"""Params generator for climo step.

Each function return a dict of params needed by run step function of ploto.
    {
        "task": task dict,
        "work_dir": work dir string,
        "config": config dict,
    }

"""
import datetime
import importlib
from typing import Callable


def generate_fetcher_params(drag_run_config: dict, fields: list) -> dict:
    """generate edp_fetcher.get_data params

    Parameters
    ----------
    drag_run_config: dict
        drag run config assigned by airflow trigger_bag's --conf option.
    fields: list
        fields name list

    Return
    ------
    dict
        ploto.fetcher.edp_fetcher.get_data params
    """
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    start_date = datetime.datetime.strptime(common_config["date"]["start"], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config["date"]["end"], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    file_prefix = "{atm_id}.{case_id}".format(
        atm_id=common_config["model_info"]["atm_id"],
        case_id=common_config["case_info"]["id"],
    )

    step1_file_prefix = "{file_prefix}.step1".format(
        file_prefix=file_prefix
    )

    task_config = {
        "step_type": "fetcher",
        "common": common_config,
        "type": "ploto.fetcher.edp_fetcher",
        "query_param": {
            "type": "nc",
            "output_dir": "./data",
            "file_prefix": step1_file_prefix,
            "date_range": date_range,
            "field_names": fields,
            "datedif": "h0"
        },
    }
    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_cdo_select_params(drag_run_config: dict, field: str) -> dict:
    """generate `ploto.processor.cdo_processor.select.run_cdo` params

    Parameters
    ----------
    drag_run_config: dict
        drag run config assigned by airflow trigger_bag's --conf option.
    field: str
        field name

    Return
    ------
    dict
        `ploto.processor.cdo_processor.select.run_cdo` params
    """
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    file_prefix = "{atm_id}.{case_id}".format(
        atm_id=common_config["model_info"]["atm_id"],
        case_id=common_config["case_info"]["id"]
    )

    step1_file_prefix = "{file_prefix}.step1".format(
        file_prefix=file_prefix
    )

    time_range_string = "{start_date}:{end_date}".format(
        start_date=common_config["date"]["start"],
        end_date=common_config["date"]["end"],
    )
    output_file_pattern = "{file_prefix}.{name}.monthly.{time_range}.nc"

    task_config = {
        "step_type": "processor",
        "type": "ploto.processor.cdo_processor",
        "operator": "select",
        "params": {
            "name": field,
            "startdate": common_config["date"]["start"],
            "enddate": common_config["date"]["end"]
        },
        "input_files": [
            "./data/{step1_file_prefix}.*.nc".format(step1_file_prefix=step1_file_prefix)
        ],
        "output_file": output_file_pattern.format(
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


def generate_gw_fetcher_params(drag_run_config: dict, fields: list) -> dict:
    """generate edp fetcher params for gw.
    """
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    start_date = datetime.datetime.strptime(common_config["date"]["start"], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(common_config["date"]["end"], "%Y-%m-%d")
    date_range = [start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")]

    step2_file_prefix = "{model_id}.{case_id}.step2".format(
        model_id=common_config["model_info"]["id"],
        case_id=common_config["case_info"]["id"]
    )

    task_config = {
        "step_type": "fetcher",
        "common": common_config,
        "type": "ploto.fetcher.edp_fetcher",
        "query_param": {
            "type": "nc",
            "output_dir": "./data",
            "file_prefix": step2_file_prefix,
            "date_range": date_range,
            "field_names": fields,
            "datedif": "h0"
        }
    }

    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_gw_cdo_select_params(drag_run_config: dict, field: str) -> dict:
    """generate cdo select params for gw.
    """
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    step2_file_prefix = "{model_id}.{case_id}.step2".format(
        model_id=common_config["model_info"]["id"],
        case_id=common_config["case_info"]["id"]
    )

    task_config = {
        "step_type": "processor",
        "type": "ploto.processor.cdo_processor",
        "operator": "select",
        "params": {
            "name": "gw",
        },
        "input_files": [
            "./data/{step2_file_prefix}.*.nc".format(step2_file_prefix=step2_file_prefix)
        ],
        "output_file": "./{model_id}.{case_id}.gw.nc".format(
            model_id=common_config["model_info"]["id"],
            case_id=common_config["case_info"]["id"]),
    }

    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_plotter_params(drag_run_config: dict) -> dict:
    """generate `ploto.plotter.esmdiag_plotter.run_plotter` params

    Parameters
    ----------
    drag_run_config: dict
        drag run config assigned by airflow trigger_bag's --conf option.

    Return
    ------
    dict
        `ploto.plotter.esmdiag_plotter.run_plotter` params
    """
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]
    figure_config = drag_run_config["figure_config"]

    task_config = {
        "step_type": "plotter",
        "type": "ploto.plotter.esmdiag_plotter",
        "metric": figure_config["metric"],
        "figure": figure_config["name"],
        "common": common_config,
    }

    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }


def generate_esmdiag_vinterp_processor_params(
        model: str,
) -> Callable[[dict, list], dict]:
    try:
        model_module = importlib.import_module(
            "ploto_airflow.esmdiag.models.{model}".format(model=model)
        )
        return model_module.generate_vinterp_processor_params
    except ImportError:
        raise
