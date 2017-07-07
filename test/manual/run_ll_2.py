import ftplib
import subprocess
import click
import json


def run_command():
    print('run command start')
    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-i',  '-c', 'ncl --help'],
        start_new_session=True
    )
    stdout, stderr = ncl_pipe.communicate()
    print(ncl_pipe)
    print(stdout)
    print(stderr)
    print('run command done')


def main():
    run_command()
    run_command()


if __name__ == "__main__":
    main()
