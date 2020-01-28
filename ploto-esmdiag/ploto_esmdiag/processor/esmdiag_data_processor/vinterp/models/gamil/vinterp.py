# coding: utf-8
from pathlib import Path
import subprocess
import os

from ploto.logger import get_logger


def run_task(task, work_dir, config) -> bool:
    """

    :param task:
        {
            'type': 'ploto_esmdiag.processor.esmdiag_data_processor',
            'action: 'vinterp',
            'model': 'gamil',
            'tasks': [
                {
                    "input_file_path": "",
                    "ps_file_path": "",
                    "output_file_path": "",
                    "var_name": "U",
                    "levels": [1000, 925, 850, 775, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
                    "interp_type": "linear",
                    "extrap": "false"
                },
            ]
        }
    :param work_dir:
    :param config:
    :return:
    """
    logger = get_logger()

    vinterp_ncl_script = Path(Path(__file__).parent, "vinterp.ncl")

    for vinterp_task in task["tasks"]:
        input_file_path = str(Path(Path(work_dir), vinterp_task["input_file_path"]))
        output_file_path = str(Path(Path(work_dir), vinterp_task["output_file_path"]))
        ps_file_path = str(Path(Path(work_dir), vinterp_task["ps_file_path"]))

        var_name = vinterp_task["var_name"]
        levels = vinterp_task["levels"]

        interp_type = vinterp_task["interp_type"]
        if interp_type == "linear":
            interp_type = 1
        elif interp_type == "log":
            interp_type = 2
        else:
            logger.error("interp type is not supported:", interp_type)
            return False

        extrap = vinterp_task["extrap"]

        esmdiag_env = os.environ.copy()
        esmdiag_env["ESMDIAG_ROOT"] = config["esmdiag"]["root"]

        logger.info("run vinterp.ncl for {var_name}...".format(var_name=var_name))
        ncl_command = [
            'ncl -Q '
            'ps_path=\\"{ps_path}\\" '
            'var_path=\\"{var_path}\\" '
            'var_name=\\"{var_name}\\" '
            'plevs=\\(/{plevs}/\\) '
            'interp_type={interp_type} '
            'extrap={extrap} '
            'out_path=\\"{out_path}\\" '
            '{ncl_script}'.format(
                ps_path=ps_file_path,
                var_path=input_file_path,
                var_name=var_name,
                plevs=",".join([str(level) for level in levels]),
                interp_type=interp_type,
                extrap=extrap,
                out_path=output_file_path,
                ncl_script=vinterp_ncl_script)]
        logger.info(' '.join(ncl_command))
        ncl_result = subprocess.run(
            ncl_command,
            env=esmdiag_env,
            # start_new_session=True,
            shell=True,
        )

        logger.info("run vinterp.ncl for {var_name}...done".format(var_name=var_name))
    return True
