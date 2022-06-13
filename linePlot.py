import pandas as pd
import plotly.express as pe

df = pd.read_csv("line_chart.csv")
fig =pe.line( df, x="Year", y="Per capita income" , color="Country", title="Per Capita Income")
fig.show()