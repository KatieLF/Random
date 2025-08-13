

import glob
import pandas as pd

#import all csv files
csv_files = glob.glob('BLANK.csv')
#call csv files to make sure they are imported correctly
csv_files

#append all the csv files at once
for file in csv_files:
    df = pd.read_csv(file)
    df_csv_append = df_csv_append.append(df, ignore_index=True)
    
df_csv_append
