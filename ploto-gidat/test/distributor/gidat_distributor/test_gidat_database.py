# coding=utf-8
import warnings


def test_gidat_database():
    warnings.warn("this does not worked", DeprecationWarning)
    from ploto_gidat.distributor import gidat_distributor

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

    gidat_distributor.run_distributor(task, '', config)


if __name__ == "__main__":
    test_gidat_database()
