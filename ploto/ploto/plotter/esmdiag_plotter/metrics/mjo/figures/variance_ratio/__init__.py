# coding: utf-8
"""
mjo/variance_ratio

output:
    pattern:
        {model_id}.{case_id}.mjo.variance_ratio.{season}.pdf

        season: summer, winter

    example:
        FGOALS-g3.gamil_wu_run11.mjo.variance_ratio.summer.pdf
        FGOALS-g3.gamil_wu_run11.mjo.variance_ratio.winter.pdf

"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_variance_ratio.ncl")
