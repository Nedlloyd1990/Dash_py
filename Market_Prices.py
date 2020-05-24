import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import os

list1=["ADANIPORTS", "ASIANPAINT","BAJAJ-AUTO","BAJFINSV","BPCL","CIPLA","DRREDDY","GAIL"]
data1=[]
data_dict=[data1.append(i1) for i1 in list1]
print(data_dict)

app = dash.Dash(__name__)

app.layout = html.Div([


    html.Div([dcc.Dropdown(
        id="stock_input",
        options=[{'label': i, 'value': i} for i in data1],value="ASIANPAINT"
    )      
  ]),  

   
    html.Div([ 
        html.Div([    
            dcc.Graph(
                id="Stock_Chart",
                )
        ],className="six columns"),
    ], className="row"),
])

@app.callback(dash.dependencies.Output("Stock_Chart","figure"),
               [dash.dependencies.Input("stock_input", "value")]
               )

def update_fig(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value +".NS.csv")

    data=[]
    trace_close=go.Scatter(x=list(df['Date']),
                            y=list(df['Close']),
                            name="Close",
                            mode= 'lines',
                            line=dict(color="#f44242"))

    data.append(trace_close)

    layout ={"title": input_value}
    return{
        "data":data,
        "layout":layout
    }

if __name__ == '__main__':
    app.run_server(port=8000)

#######