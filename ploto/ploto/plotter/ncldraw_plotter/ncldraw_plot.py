import subprocess
import click
import json


@click.command()
@click.option('--param', help='json param string')
def ncldraw_plot(param):
    param_object = json.loads(param)
    task_file = param_object['task_file']
    time_level = param_object['time_level']

    ncldraw_result = subprocess.run(
        ['/bin/bash', '-i', '-c', 'ncldraw {task_file} {time_level}'.format(
            task_file=task_file,
            time_level=time_level
        )]
    )
    # print(ncldraw_result.stdout)
    # print(ncldraw_result.stderr)


if __name__ == "__main__":
    ncldraw_plot()
