# coding=utf-8
from flask import Blueprint

api_v1_app = Blueprint('api_v1_app', __name__, template_folder='template')

import ploto_server.api.metgui
import ploto_server.api.plot
