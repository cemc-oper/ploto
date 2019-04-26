# coding: utf-8


def test_select():
    task = {
        'type': 'cdo_processor',
        'operator': 'select',
        'params': {
            'name': 'PS',
            'startdate': '1981-01-01',
            'enddate': '1982-01-01'
        },
        'input_files': [
            './data/GAMIL.gamil_wu_run11*.nc'
        ],
        'output_file': './temp/GAMIL.gamil_wu_run11.PS.monthly.1981-01-01:1981-12-31.nc',
    }
    work_dir = '/home/hujk/clusterfs/wangdp/temp'
    config = {}

    from ploto.processor.cdo_processor.select import run_cdo
    run_cdo(task, work_dir, config)


if __name__ == "__main__":
    test_select()
