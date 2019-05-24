# coding: utf-8


def generate_steps(file_prefix, output_file_pattern, time_range_string, common_config):
    steps = []
    # PRC.anomaly
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'anomaly',
        'input_file': output_file_pattern.format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
    })

    steps.extend(_generate_steps_for_area_avg(file_prefix, output_file_pattern, time_range_string, common_config))
    steps.extend(_generate_steps_for_lat_avg(file_prefix, output_file_pattern, time_range_string, common_config))
    steps.extend(_generate_steps_for_lon_avg(file_prefix, output_file_pattern, time_range_string, common_config))
    return steps


def _generate_steps_for_area_avg(file_prefix, output_file_pattern, time_range_string, common_config):
    steps = []
    # PRC.anomaly.area_avg_IO
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'area_avg',
        'start_lon': 75.0,
        'end_lon': 100.0,
        'start_lat': -10.0,
        'end_lat': 5.0,
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.area_avg_IO.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config
    })

    # PRC.anomaly.area_avg_IO.detrended
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.area_avg_IO.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.area_avg_IO.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config,
    })

    # PRC.anomaly.area_avg_IO.detrended.filter
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': "{file_prefix}.{name}.daily.anomaly.area_avg_IO.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.area_avg_IO.detrended.filtered.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'var_name': 'PRC',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })
    return steps


def _generate_steps_for_lat_avg(file_prefix, output_file_pattern, time_range_string, common_config):
    steps = []
    # PRC.daily.anomaly.lat_avg_lon_band
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'lat_avg',
        'start_lat': -10.0,
        'end_lat': 10.0,
        'use_wgt_lat': 'False',
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lat_avg_lon_band.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config
    })

    # PRC.anomaly.lat_avg_lon_band.detrended
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.lat_avg_lon_band.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lat_avg_lon_band.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config,
    })

    # PRC.daily.anomaly.lat_avg_lon_band.detrended.filtered
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': "{file_prefix}.{name}.daily.anomaly.lat_avg_lon_band.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lat_avg_lon_band.detrended.filtered.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'var_name': 'PRC',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })
    return steps


def _generate_steps_for_lon_avg(file_prefix, output_file_pattern, time_range_string, common_config):
    steps = []
    # PRC.daily.anomaly.lon_avg_lat_band
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'lon_avg',
        'start_lon': 80.0,
        'end_lon': 100.0,
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lon_avg_lat_band.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config
    })

    # PRC.anomaly.lon_avg_lat_band.detrended
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'detrend',
        'dim': 0,
        'var_name': 'PRC',
        'input_file': "{file_prefix}.{name}.daily.anomaly.lon_avg_lat_band.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lon_avg_lat_band.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'common_config': common_config,
    })

    # PRC.daily.anomaly.lon_avg_lat_band.detrended.filtered
    steps.append({
        'step_type': 'processor',
        'type': 'esmdiag_data_processor',
        'action': 'filter',
        'input_file': "{file_prefix}.{name}.daily.anomaly.lon_avg_lat_band.detrended.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'output_file': "{file_prefix}.{name}.daily.anomaly.lon_avg_lat_band.detrended.filtered.{time_range}.nc".format(
            file_prefix=file_prefix,
            time_range=time_range_string,
            name='PRC'),
        'var_name': 'PRC',
        'method': 'butterworth',
        'low_pass': 0.01,
        'high_pass': 0.05,
    })
    return steps
