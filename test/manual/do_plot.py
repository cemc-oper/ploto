import subprocess
import json
import ftplib


def download_data(file_path):
    ftp = ftplib.FTP("10.28.32.114")
    ftp.login("wangdp", "perilla")
    ftp.cwd('/srv/files/ftp/GRAPES_GFS_ORIG_2017070400')
    ftp.retrbinary(
        'RETR {file_path}'.format(file_path=file_path),
        open('{file_path}'.format(file_path=file_path), 'wb').write)
    ftp.quit()


def save_ncl_script(ncl_script_path, ncl_script):
    with open(ncl_script_path, 'w') as f:
        f.write(ncl_script)


def get_ncl_script():
    return """begin
    f = addfile(file_path,"r")

    var = f->TMP_P0_L1_GLL0

    wks = gsn_open_wks("png", "tmp.png")

    res = True
    res@tiMainString = "TEMP"
    res@cnFillOn = True

    plot = gsn_csm_contour_map(wks,var,res)

end
"""


def main():
    param = {
        'file_path': "gmf.gra.2017070400006.grb2",
        'ncl_script_path': "draw.ncl"
    }

    download_data(param['file_path'])
    save_ncl_script(param['ncl_script_path'], get_ncl_script())

    param_string = json.dumps(param)

    subprocess.run(
        ['/home/wangdp/nwpc/gidat/plot/workspace/env/bin/python',
         '/home/wangdp/nwpc/gidat/plot/workspace/gidat-plot/test/manual/test_plot.py',
         '--param={param_string}'.format(param_string=param_string)]
    )


if __name__ == "__main__":
    main()
