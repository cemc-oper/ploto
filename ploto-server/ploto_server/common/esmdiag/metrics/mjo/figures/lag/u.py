# coding: utf-8


def generate_steps(file_prefix, output_file_pattern, time_range_string, common_config, model_id, case_id):
    steps = []
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'anomaly',
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='U'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='U'),
    })

    # u.anomaly.vinterp
    var_file_pattern = "{model}.{case_id}.{name}.daily.anomaly.{time_range_string}.nc"
    ps_file_path = output_file_pattern.format(
        file_prefix=file_prefix,
        time_range=time_range_string,
        name='PS'
    )
    u_levels = [850, 200]
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'vinterp',
        'model': 'gamil',
        'tasks': [
            {
                "input_file_path": var_file_pattern.format(
                    model=model_id,
                    case_id=case_id,
                    name="U",
                    time_range_string=time_range_string,
                ),
                "ps_file_path": ps_file_path,
                "output_file_path": ("{model}.{case_id}.{name}.daily.anomaly."
                                     "vinterp{levels}.{time_range_string}.nc").format(
                    model=model_id,
                    case_id=case_id,
                    name='U',
                    levels=":".join([str(level) for level in u_levels]),
                    time_range_string=time_range_string
                ),
                "var_name": "U",
                "levels": u_levels,
                "interp_type": "linear",
                "extrap": "True"
            },
        ],
        'common': common_config,
    })

    steps.extend(_generate_steps_for_lat_avg(time_range_string, common_config, model_id, case_id, u_levels))
    steps.extend(_generate_steps_for_lon_avg(time_range_string, common_config, model_id, case_id, u_levels))

    return steps


def _generate_steps_for_lat_avg(time_range_string, common_config, model_id, case_id, u_levels):
    steps = []
    # U.daily.anomaly.vinterp.lat_avg_lon_band
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'lat_avg',
        'start_lat': -10.0,
        'end_lat': 10.0,
        'use_wgt_lat': 'False',
        'var_name': 'U',
        'input_file': "{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}.{time_range_string}.nc".format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file':  ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                         "lat_avg_lon_band.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'common_config': common_config,
    })

    # U.daily.anomaly.vinterp.lat_avg_lon_band.detrended
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'var_name': 'U',
        'input_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                       "lat_avg_lon_band.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                        "lat_avg_lon_band.detrended.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string,
        ),
        'common_config': common_config,
    })

    # U.daily.anomaly.lat_avg_lon_band.detrended.filtered
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                       "lat_avg_lon_band.detrended.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                        "lat_avg_lon_band.detrended.filtered.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'var_name': 'U',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })
    return steps


def _generate_steps_for_lon_avg(time_range_string, common_config, model_id, case_id, u_levels):
    steps = []
    # U.daily.anomaly.vinterp.lon_avg_lat_band
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'lon_avg',
        'start_lon': 80.0,
        'end_lon': 100.0,
        'var_name': 'U',
        'input_file': "{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}.{time_range_string}.nc".format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file':  ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                         "lon_avg_lat_band.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'common_config': common_config,
    })

    # U.daily.anomaly.vinterp.lon_avg_lat_band.detrended
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'var_name': 'U',
        'input_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                       "lon_avg_lat_band.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                        "lon_avg_lat_band.detrended.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string,
        ),
        'common_config': common_config,
    })

    # U.daily.anomaly.lon_avg_lat_band.detrended.filtered
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                       "lon_avg_lat_band.detrended.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'output_file': ("{model}.{case_id}.{name}.daily.anomaly.vinterp{levels}."
                        "lon_avg_lat_band.detrended.filtered.{time_range_string}.nc").format(
            model=model_id,
            case_id=case_id,
            name='U',
            levels=":".join([str(level) for level in u_levels]),
            time_range_string=time_range_string
        ),
        'var_name': 'U',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })
    return steps
