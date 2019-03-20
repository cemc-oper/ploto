# coding=utf-8
import click


@click.command()
@click.option('-c', '--config-file', help='config file path')
def runserver(config_file):
    """
    DESCRIPTION
        Run nwpc monitor broker.
    """

    from ploto_server.app import create_app
    app = create_app(config_file)

    app.run(
        host=app.config['BROKER_CONFIG']['host']['ip'],
        port=app.config['BROKER_CONFIG']['host']['port']
    )


if __name__ == '__main__':
    runserver()
