import pandas as p 
import plotly.express as px
import csv
import plotly.graph_objects as go
df=p.read_csv("dta.csv")
studentdf=df.loc[df["student_id"]=="TRL_abc"]
print(studentdf.groupby("level")["attempt"].mean())
figure=go.Figure(go.Bar(
    x=studentdf.groupby("level")["attempt"].mean(),
    y=["level","level2","level3","level4"],
    orientation="h"
))
figure.show()
