# coding=utf-8
from flask import Blueprint, jsonify

main_app = Blueprint('main_app', __name__, template_folder='template')


@main_app.route('/')
def get_index_page():
    return jsonify({
        'status': 'ok'
    })
