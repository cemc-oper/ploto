# coding=utf-8
import time
import json

import requests


if __name__ == "__main__":
    plot_task = {
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
    result = requests.post("http://localhost:8085/api/v1/gidat/plot-metgui", data={
        'plot_task': json.dumps(plot_task)
    })
    print(result.content)
