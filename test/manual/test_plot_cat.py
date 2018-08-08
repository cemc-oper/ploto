import ftplib
import subprocess
import click
import json


def get_data(file_path):
    ftp = ftplib.FTP("10.28.32.114")
    ftp.login("wangdp", "perilla")
    ftp.cwd('/srv/files/ftp/GRAPES_GFS_ORIG_2017070400')
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=file_path),
        open('{file_path}'.format(file_path=file_path), 'wb').write)
    ftp.quit()


@click.command()
@click.option('--param', help='json param string')
def main(param):
    param_object = json.loads(param)
    file_path = param_object['file_path']  # "gmf.gra.2017070400006.grb2"
    get_data(file_path)

    ncl_script = param_object['ncl_script']  # get_ncl_script()

    echo_pipe = subprocess.Popen(
        """cat <<EOF
        {ncl_script}
EOF""".format(ncl_script=ncl_script),
        stdout=subprocess.PIPE,
        shell=True
    )

    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-i', '-c', 'ncl file_path=\\"{file_path}\\"'.format(file_path=file_path)],
        stdin=echo_pipe.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    echo_pipe.stdout.close()
    (cdp_output, cdp_error) = ncl_pipe.communicate()
    return_code = ncl_pipe.returncode
    print(return_code)
    print(cdp_output.decode())
    print(cdp_error.decode())


if __name__ == "__main__":
    main()
