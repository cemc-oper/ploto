# coding: utf-8
"""
mjo/combined_eof

output:
    pattern:
        {model_id}.{case_id}.mjo.index.pdf

    example:
        FGOALS-g3.gamil_wu_run11.mjo.index.pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_combined_eof.ncl")
