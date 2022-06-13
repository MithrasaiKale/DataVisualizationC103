import plotly.express as pe
import pandas as pd

df = pd.read_csv("Data.csv")
fig=pe.bar(df, x="Country", y="InternetUsers", color="Country")
fig.show()