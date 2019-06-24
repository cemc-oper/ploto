# coding: utf-8
"""
climo/precip

output:
    pattern:
        {model_atm_id}.{case_id}.climo.PRECT.{season}.pdf
        {model_atm_id}.{case_id}.climo.PRECC_vs_PRECL.{season}.pdf

        season: ANN, JJA, DJF

    example:
        GAMIL.gamil_wu_run11.climo.PRECT.ANN.pdf
        GAMIL.gamil_wu_run11.climo.PRECT.DJF.pdf
        GAMIL.gamil_wu_run11.climo.PRECT.JJA.pdf
        GAMIL.gamil_wu_run11.climo.PRECC_vs_PRECL.ANN.pdf
        GAMIL.gamil_wu_run11.climo.PRECC_vs_PRECL.DJF.pdf
        GAMIL.gamil_wu_run11.climo.PRECC_vs_PRECL.JJA.pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_precip.ncl")
