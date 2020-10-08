import pandas as pd
import numpy as np

import glob
print(glob.glob("*.csv"))
all_data = pd.DataFrame()
print(all_data)
for f in glob.glob("*.csv"):
    df = pd.read_csv(f)
    #print(df)
