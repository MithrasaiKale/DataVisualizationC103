import pandas as pd
import plotly.express as pe

df = pd.read_csv("Data.csv")
fig=pe.scatter(df, x="Population", y="Per capita", color="Country", size="Percentage", size_max=60)
fig.show()