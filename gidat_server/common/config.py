"""
config.py

use environment var
"""
import os
import yaml


class Config(object):
    def __init__(self, config_path):
        with open(config_path) as config_file:
            config_dict = yaml.load(config_file)
            broker_config = config_dict['broker']
            self.BROKER_CONFIG = broker_config

            if 'debug' in broker_config:
                debug_config = broker_config['debug']
                if 'flask_debug' in debug_config:
                    flask_debug = debug_config['flask_debug']
                    if flask_debug is True:
                        self.DEBUG = True
                    elif flask_debug is not True:
                        self.DEBUG = False
    @classmethod
    def load_config(cls, config_file_path: None or str = None):
        if config_file_path is None:
            if 'GIDAT_SERVER_CONFIG' in os.environ:
                config_file_path = os.environ['GIDAT_SERVER_CONFIG']
            else:
                return None

        print("config file path:", config_file_path)

        config_object = Config(config_file_path)

        return config_object
