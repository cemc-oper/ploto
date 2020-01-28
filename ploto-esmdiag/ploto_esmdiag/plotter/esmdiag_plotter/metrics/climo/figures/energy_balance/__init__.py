# coding: utf-8
"""
climo/energy_balance

output:
    pattern:
        {model_atm_id}.{case_id}.climo.energy_balance..pdf

    example:
        GAMIL.gamil_wu_run11.climo.energy_balance..pdf

"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_energy_balance.ncl")

