# coding: utf-8
"""
climo/zonal_mean

output:
    pattern:
        {model_atm_id}.{case_id}.zonal_mean.T.{season}.pdf
        {model_atm_id}.{case_id}.zonal_mean.Q.{season}.pdf
        {model_atm_id}.{case_id}.zonal_mean.U.{season}.pdf

        season: ANN, JJA, DJF

    example:
        GAMIL.gamil_wu_run11.climo.zonal_mean.Q.ANN.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.Q.DJF.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.Q.JJA.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.T.ANN.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.T.DJF.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.T.JJA.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.U.ANN.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.U.DJF.pdf
        GAMIL.gamil_wu_run11.climo.zonal_mean.U.JJA.pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_zonal_mean.ncl")
