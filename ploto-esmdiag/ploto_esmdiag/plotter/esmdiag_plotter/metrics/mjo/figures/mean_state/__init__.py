# coding: utf-8
"""
mjo/mean_state

output:
    pattern:
        {model_id}.{case_id}.mjo.mean_state.{season}.pdf

        season: summer, winter

    example:
        FGOALS-g3.gamil_wu_run11.mjo.mean_state.summer.pdf
        FGOALS-g3.gamil_wu_run11.mjo.mean_state.winter.pdf

"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_mean_state.ncl")
