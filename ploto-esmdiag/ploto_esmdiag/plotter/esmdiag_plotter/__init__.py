# coding: utf-8


def run_plotter(task, work_dir, config) -> bool:
    """

    :param task:
        {
            metric: 'climo',
            figure: 'precip',
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
    from ploto_esmdiag.plotter.esmdiag_plotter import metric_task
    metric_task.run_task(task, work_dir, config)
    return True
