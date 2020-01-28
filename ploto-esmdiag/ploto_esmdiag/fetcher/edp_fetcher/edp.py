#!/usr/bin/python
# coding: utf-8
import sys
import json

import click


def run_dep(query, edp_module_path='/home/hujk/pyProject/'):
    sys.path.append(edp_module_path)
    import handle_query_nc
    query_json = json.loads(query)
    print(query_json)
    handle_query_nc.parse_query_nc(query_json)


@click.command()
@click.option('--edp-module-path', help='edp module path', default='/home/hujk/pyProject/')
@click.argument('query')
def cli(edp_module_path, query):
    run_dep(query, edp_module_path)


if __name__ == '__main__':
    cli()
