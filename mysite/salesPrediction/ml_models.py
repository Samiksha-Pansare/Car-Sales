import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta,date
import numpy as np

import fbprophet
from prophet import Prophet
from pandas import to_datetime

path = "../data/monthly-car-sales-v3-2013-2020.csv"
df1 = pd.read_csv(path ,encoding='ISO-8859-1')
from datetime import datetime
df1["Date"] = 0
for row in df1.index:
  df1["Date"][row] = datetime.strptime(df1["Month"][row], '%d-%m-%Y').date()
def create_df(ogdf,model, region):
    df = ogdf.drop(ogdf.index[ogdf['Region'] != region])
    df = df.drop(df.index[df['Model'] != model])
    black_df = df.drop(df.index[df['Color'] != 'Black']).groupby(['Date']).Sales.sum().reset_index()
    white_df = df.drop(df.index[df['Color'] != 'White']).groupby(['Date']).Sales.sum().reset_index()
    grey_df = df.drop(df.index[df['Color'] != 'Grey']).groupby(['Date']).Sales.sum().reset_index()
    return black_df,white_df,grey_df

# Try calling the create_df function
black_df,white_df,grey_df = create_df(df1,"Maruti Suzuki Dzire", "Mumbai")
print(white_df)