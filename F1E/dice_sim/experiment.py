import sys

sys.path.insert(0, "../dice_sim")

import pandas as pd

from main import Dice, launch_experiment

d6 = Dice(6)

output = pd.DataFrame()
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)
output = output.append(launch_experiment(d6, 100, 1), ignore_index=True)


output.to_excel("dice_exp.xlsx", sheet_name="rolls")
