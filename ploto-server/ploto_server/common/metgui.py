# coding: utf-8
import time
from pathlib import Path


def create_message_from_plot_task(plot_task: dict) -> dict:
    """

    :param plot_task:
        {
          "data_file_path": "/space/workspace/data/42946/42955.grb2",
          "image_path": "/space/workspace/product/grapes/42947/42955.png",
          "plot_data_list": [
            {
              "file_name": "1541.grb2",
              "query_param": {
                "config": {
                  "date": "20130817",
                  "expID": "G1600010",
                  "groupname": "DYN",
                  "levelist": "0",
                  "levtype": "2",
                  "param": "hcc",
                  "savePath": "./ddps",
                  "step": "6",
                  "time": "1200,12:00"
                },
                "password": "admin",
                "username": "admin",
                "operation": "extractdownload",
              }
            }
          ],
          "plot_file_id": "42955",
          "plot_set_id": "42951",
          "task_file_list": [
            {
              "file_content": "<?xml version='1.0' encoding='UTF-8'?>\n<task>\n    <workstation output=\"42955.png\" backgroundcolor=\"white\" foregroundcolor=\"black\" colormap=\"color_tcloud\" addcycle=\"true\">\n        <plotmanager type=\"normal\">\n            <plot type=\"map\" resourcefile=\"grapes/map.xml\">\n                <plot type=\"textitem\">\n                    <txString value=\"high cloud cover--hcc\"/>\n                    <txFontHeightF value=\"0.013\"/>\n                    <txJust value=\"CenterLeft\"/>\n                    <boundary txJust=\"TopLeft\" yAdjust=\"0.011\" xAdjust=\"0.05\"/>\n                </plot>\n                <plot type=\"textitem\">\n                    <txString value=\"%tl%vh\"/>\n                    <txFontHeightF value=\"0.013\"/>\n                    <txJust value=\"CenterRight\"/>\n                    <boundary txJust=\"TopRight\" yAdjust=\"0.011\" xAdjust=\"-0.05\"/>\n                </plot>\n                <plot type=\"textitem\">\n                    <txString value=\"GRAPES 0.5~S~o~N~*0.5~S~o~N~ Valid Time: %tl + %vh hrs\"/>\n                    <txFontHeightF value=\"0.011\"/>\n                    <txJust value=\"CenterLeft\"/>\n                    <boundary txJust=\"BottomLeft\" yAdjust=\"-0.011\" xAdjust=\"0.15\"/>\n                </plot>\n                <plot type=\"contour\" datadir=\"/space/workspace/data/42946\" resourcefile=\"toolkits/diagnostic/level_3/hcc_fill.xml\" datafile=\"42955.grb2\">\n                    <parameter center=\"BABJ\" parameternumber=\"5\" parametercategory=\"6\" leveltype=\"2\" level=\"0\" model=\"GRAPES\" discipline=\"0\" validhourlist=\"6\"/>\n                </plot>\n            </plot>\n        </plotmanager>\n    </workstation>\n</task>\n",
              "file_path": "../script/42947_hcc_Fill__Global_2013081712_6_0.xml"
            }
          ],
          "time_level": "2013081712"
        }
    :return:
    """

    # data fetcher
    plot_data_list = plot_task['plot_data_list']
    data_file_list = []
    file_config_list = []
    for a_plot_data in plot_data_list:
        file_config = {
            'type': 'ddps_fetcher'
        }
        file_config.update(a_plot_data)
        file_config_list.append(file_config)
        data_file_list.append(a_plot_data['file_name'])
    data_fetcher_config = file_config_list

    # pre-processor
    data_file_name = Path(plot_task['data_file_path']).name
    cat_file_task = {
        'type': 'cat_file_processor',
        'file_list': data_file_list,
        'target': data_file_name
    }
    pre_processor_config = [cat_file_task]

    # plotter
    task_files = []
    for an_item in plot_task['task_file_list']:
        task_files.append({
            'file_content': an_item['file_content'],
            'file_path': str(Path(an_item['file_path']).name)
        })

    image_name = str(Path(plot_task['image_path']).name)
    plotter_config = {
        'type': 'ncldraw_plotter',
        'task_files': task_files,
        'time_level': plot_task['time_level'],
        'image_path': str(Path(plot_task['image_path']).name),
    }

    # post_processor
    post_processor_config = [
        {
            'type': 'copy_file_processor',
            'files': [
                {
                    'from': image_name,
                    'to': plot_task['image_path']
                }
            ]
        },
        {
            'type': 'copy_file_processor',
            'files': [
                {
                    'from': data_file_name,
                    'to': plot_task['data_file_path']
                }
            ]
        }
    ]

    task = {
        'app': 'gidat-plot',
        'type': 'gidat-plot',
        'timestamp': time.time(),
        'data': {
            'data_fetcher': data_fetcher_config,
            'pre_processor': pre_processor_config,
            'plotter': plotter_config,
            'post_processor': post_processor_config
        }
    }

    return task
