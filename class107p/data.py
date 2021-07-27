import pandas as p 
import plotly.express as px 
import csv 
import plotly.graph_objects as go 
df=p.read_csv("dta.csv")
print(df.groupby("level")["attemt"].mean())
figure=go.figure(go.bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"]
    orientation="h"
))
figure.show()