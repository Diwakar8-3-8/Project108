import plotly.express as pe
import plotly.figure_factory as pff
import pandas as pd
import csv

df=pd.read_csv("data.csv")
fig = pff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()