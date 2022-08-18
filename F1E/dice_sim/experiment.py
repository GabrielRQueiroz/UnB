import sys

sys.path.insert(0, "../dice_sim")

import pandas as pd

from main import Dice, launch_experiment

d6 = Dice(6)

pd.concat(
    [pd.DataFrame([launch_experiment(d6, 100, 1)]) for i in range(10)],
    ignore_index=True,
).transpose().to_excel("./results/launch_experiment.xlsx")
