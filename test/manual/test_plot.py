import ftplib
import subprocess
import click
import json


@click.command()
@click.option('--param', help='json param string')
def main(param):
    param_object = json.loads(param)
    file_path = param_object['file_path']  # "gmf.gra.2017070400006.grb2"
    ncl_script = param_object['ncl_script_path']  # get_ncl_script()

    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-i', '-c', 'ncl file_path=\\"{file_path}\\" {ncl_script}'.format(
            file_path=file_path,
            ncl_script=ncl_script
        )],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    (cdp_output, cdp_error) = ncl_pipe.communicate()
    return_code = ncl_pipe.returncode
    print(return_code)
    print(cdp_output.decode())
    print(cdp_error.decode())


if __name__ == "__main__":
    main()
