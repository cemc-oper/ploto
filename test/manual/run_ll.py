import ftplib
import subprocess
import click
import json


def main():
    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-c', 'll'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    (cdp_output, cdp_error) = ncl_pipe.communicate()
    return_code = ncl_pipe.returncode
    print(return_code)
    print(cdp_output.decode())
    print(cdp_error.decode())

    ncl_pipe = subprocess.Popen(
        ['/bin/bash', '-c', 'll'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    (cdp_output, cdp_error) = ncl_pipe.communicate()
    return_code = ncl_pipe.returncode
    print(return_code)
    print(cdp_output.decode())
    print(cdp_error.decode())


if __name__ == "__main__":
    main()
