# coding: utf-8


def test_sub():
    task = {
        'type': 'cdo_processor',
        'operator': 'sub',
        'params': [
            {
                'type': 'file',
                'value': 'GAMIL.gamil_wu_run11.OLR.daily.1979-01-01:1980-12-31.nc',
            },
            '-timmean',
            {
                'type': 'file',
                'value': 'GAMIL.gamil_wu_run11.OLR.daily.1979-01-01:1980-12-31.nc',
            },
        ],
        'output_file': 'GAMIL.gamil_wu_run11.OLR.daily.anomaly.1979-01-01:1980-12-31.nc',
    }
    work_dir = '/home/hujk/clusterfs/wangdp/temp/temp'
    config = {}

    from ploto.processor.cdo_processor.sub import run_cdo
    run_cdo(task, work_dir, config)


if __name__ == "__main__":
    test_sub()
