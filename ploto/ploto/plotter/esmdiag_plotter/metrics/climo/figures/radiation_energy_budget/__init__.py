# coding: utf-8
"""
climo/radiation_energy_budget

output:
    pattern:
        {model_atm_id}.{case_id}.climo.radiation_energy_budget..pdf

    example:
        GAMIL.gamil_wu_run11.climo.radiation_energy_budget..pdf
"""
from pathlib import Path


NCL_SCRIPT_PATH = Path(Path(__file__).parent, "plot_radiation_energy_budget.ncl")
