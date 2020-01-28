# coding: utf-8


def generate_vinterp_processor_params(
        drag_run_config: dict,
        vinterp_tasks: list,
) -> dict:
    common_config = drag_run_config["common_config"]
    work_dir = drag_run_config["work_dir"]
    worker_config = drag_run_config["worker_config"]

    var_file_pattern = "{model}.{case_id}.{name}.monthly.{start_date}:{end_date}.nc"
    ps_file_path = var_file_pattern.format(
        model='GAMIL',
        case_id=common_config["case_info"]["id"],
        name="PS",
        start_date=common_config["date"]["start"],
        end_date=common_config["date"]["end"],
    )

    for a_task in vinterp_tasks:
        name = a_task["var_name"]
        a_task["input_file_path"] = var_file_pattern.format(
            model="GAMIL",
            case_id=common_config["case_info"]["id"],
            name=name,
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        )
        a_task["ps_file_path"] = ps_file_path
        a_task["output_file_path"] = "{model}.{case_id}.{name}.monthly.vinterp{levels}.{start_date}:{end_date}.nc".format(
            model="GAMIL",
            case_id=common_config["case_info"]["id"],
            name=name,
            levels=":".join([str(level) for level in a_task["levels"]]),
            start_date=common_config["date"]["start"],
            end_date=common_config["date"]["end"],
        )

    task_config = {
        'step_type': 'processor',
        'type': 'ploto.processor.esmdiag_data_processor',
        'action': 'vinterp',
        'model': 'gamil',
        "tasks": vinterp_tasks,
        "common": common_config,
    }

    return {
        "task": task_config,
        "work_dir": work_dir,
        "config": worker_config,
    }
