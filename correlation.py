import pandas as pd
import plotly.express as px
df = pd.read_csv("Student Marks vs Days Present.csv")
scatterPlot = px.scatter(df,x="Marks In Percentage",y="Days Present")
scatterPlot.show()