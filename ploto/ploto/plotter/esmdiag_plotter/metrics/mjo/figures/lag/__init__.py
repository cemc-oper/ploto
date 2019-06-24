# coding: utf-8
"""
climo/lag

output:
    pattern:
        {model_id}.{case_id}.mjo.lag.{season}.pdf
        {model_id}.{case_id}.mjo.lag.filtered.{season}.pdf

        season: annual, summer, winter

    example:
        GAMIL.gamil_wu_run11.mjo.lag.annual.pdf
        GAMIL.gamil_wu_run11.mjo.lag.summer.pdf
        GAMIL.gamil_wu_run11.mjo.lag.winter.pdf
        GAMIL.gamil_wu_run11.mjo.lag.filtered.annual.pdf
        GAMIL.gamil_wu_run11.mjo.lag.filtered.summer.pdf
        GAMIL.gamil_wu_run11.mjo.lag.filtered.winter.pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_lag.ncl")
