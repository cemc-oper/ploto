# coding: utf-8


def test_chname():
    task = {
        'type': 'ploto.processor.cdo_processor',
        'operator': 'chname',
        'params': [
            {
                'old_name': 'PS',
                'new_name': 'PS1'
            }
        ],
        'input_file': 'GAMIL.gamil_wu_run11.PS.monthly.1981-01-01:1981-12-31.nc',
        'output_file': 'GAMIL.gamil_wu_run11.PS1.monthly.1981-01-01:1981-12-31.nc',
    }
    work_dir = '/home/hujk/clusterfs/wangdp/temp/temp'
    config = {}

    from ploto.processor.cdo_processor.chname import run_cdo
    run_cdo(task, work_dir, config)


if __name__ == "__main__":
    test_chname()
