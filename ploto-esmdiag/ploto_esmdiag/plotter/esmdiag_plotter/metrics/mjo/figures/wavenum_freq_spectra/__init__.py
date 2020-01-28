# coding: utf-8
"""
mjo/wavenum_freq_spectra

output:
    pattern:
        {model_id}.{case_id}.OLR.wavenum_freq_spectrum.{season}.pdf
        {model_id}.{case_id}.U850.wavenum_freq_spectrum.{season}.pdf

        season: summer, winter

    output:
        FGOALS-g3.gamil_wu_run11.OLR.wavenum_freq_spectrum.summer.pdf
        FGOALS-g3.gamil_wu_run11.OLR.wavenum_freq_spectrum.winter.pdf
        FGOALS-g3.gamil_wu_run11.U850.wavenum_freq_spectrum.summer.pdf
        FGOALS-g3.gamil_wu_run11.U850.wavenum_freq_spectrum.winter.pdf

"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_wavenum_freq_spectra.ncl")
