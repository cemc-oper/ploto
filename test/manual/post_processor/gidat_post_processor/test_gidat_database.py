# coding=utf-8

from gidat_plot.post_processor import gidat_post_processor

task = {
    'plot_id': 16329,
    'plot_set_id': 42617
}

config = {
    'gidat_post_processor': {
        'database': {
            'host': '10.20.67.76',
            'port': '1521',
            'user': 'metview',
            'password': 'metview',
            'database_name': 'grapesorcl',
        }
    }
}


gidat_post_processor.run_post_processor(task, '', config)
