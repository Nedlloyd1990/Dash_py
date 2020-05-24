import dash
import dash_core_components as dcc
import dash_html_components as html
import time
from collections import deque
import plotly.graph_objs as go
import random
import os
import pandas as pd



list1=["ADANIPORTS", "ASIANPAINT","BAJAJ-AUTO","BAJFINSV","BPCL","CIPLA","DRREDDY","GAIL"]
data1=[]
data_dict=[data1.append(i1) for i1 in list1]


app = dash.Dash('Stock_Charting')
app.layout = html.Div([

    dcc.Dropdown(id='stockNames',options=[{'label': i, 'value': i} for i in data1],value=['BAJFINSV','BPCL'],multi=True),

    html.Div(children=html.Div(id='graphs'))
    ])

@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('stockNames', 'value')],
    )
def update_graph(data_names):
    graphs = []
 
    for data_name in data_names:
        df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ data_name + ".NS.csv")
        data = go.Scatter(x=list(df['Date']),y=list(df['Close']),name='Scatter',fill="tozeroy",fillcolor="#6897bb")


        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            figure={'data': [data],'layout' : go.Layout(margin={'l':50,'r':1,'t':45,'b':1},title='{}'.format(data_name))}
            )))

    return graphs


if __name__ == '__main__':
    app.run_server(debug=True, port=4050)