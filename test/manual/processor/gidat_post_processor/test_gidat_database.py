# coding=utf-8
import warnings


def test_gidat_database():
    warnings.warn("this does not worked", DeprecationWarning)
    from ploto.processor import gidat_post_processor

    task = {
        'plot_id': 16329,
        'plot_set_id': 42617
    }

    config = {
        'gidat_post_processor': {
            'database': {
                'host': '-',
                'port': '-',
                'user': '-',
                'password': '-',
                'database_name': '-',
            }
        }
    }

    gidat_post_processor.run_processor(task, '', config)


if __name__ == "__main__":
    test_gidat_database()
