# coding: utf-8


def run_plotter(plotter_config, work_dir, config):
    """

    :param plotter_config:
        {
            metric: 'climo',
            figure: 'precip',
        }

    :param work_dir:
    :param config:
        {
            common: {
                model_id: "FGOALS-g3"
                model_atm_id: "GAMIL"
                model_ocn_id: "LICOM"
                model_ice_id: "CICE"
                case_id: "piControl-bugfix-licom-80368d"
                start_date: "0030-01-01"
                end_date: "0060-12-31"
            }
        }
    :return:
    """
    metric = plotter_config["metric"]
    figure = plotter_config["figure"]
