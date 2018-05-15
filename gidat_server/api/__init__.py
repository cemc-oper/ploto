# coding=utf-8
from flask import Blueprint

api_v1_app = Blueprint('api_v1_app', __name__, template_folder='template')


@api_v1_app.route('/gidat/plot', methods=['POST'])
def receive_plot():
    pass
