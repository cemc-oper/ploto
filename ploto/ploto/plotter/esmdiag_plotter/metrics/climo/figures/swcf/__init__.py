# coding: utf-8
"""
climo/swcf

output:
    pattern:
        {model_atm_id}.{case_id}.climo.LWCF.{season}.pdf

        season: ANN, JJA, DJF

    example:
        GAMIL.gamil_wu_run11.climo.SWCF.ANN.pdf
        GAMIL.gamil_wu_run11.climo.SWCF.DJF.pdf
        GAMIL.gamil_wu_run11.climo.SWCF.JJA.pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_swcf.ncl")
