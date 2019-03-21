# coding: utf-8


def run_plotter(plotter_config, work_dir, config):
    """

    :param plotter_config:
        {
            common: {
                model_info: {
                    id: "FGOALS-g3",
                    atm_id: "GAMIL",
                    ocn_id: "LICOM",
                    ice_id: "CICE",
                },
                case_info: {
                    id: "piControl-bugfix-licom-80368d",
                },
                date: {
                    start: "0030-01-01",
                    end: "0060-12-31"
                }
            },
            metric: 'climo',
            figure: 'precip',
        }

    :param work_dir:
    :param config:
        {
            'esmdiag': {
                'root': root dir
            }
        }
    :return:
    """
    metric = plotter_config["metric"]
    figure = plotter_config["figure"]
    common_config = plotter_config["common"]


