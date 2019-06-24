# coding: utf-8
"""
climo/lwcf

output:
    pattern:
        {model_atm_id}.{case_id}.climo.LWCF.{season}.pdf

        season: ANN, JJA, DJF

    example:
        GAMIL.gamil_wu_run11.climo.LWCF.ANN.pdf
        GAMIL.gamil_wu_run11.climo.LWCF.DJF.pdf
        GAMIL.gamil_wu_run11.climo.LWCF.JJA.pdf


"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_lwcf.ncl")
