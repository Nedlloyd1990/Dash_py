import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import datetime
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import os
import plotly.express as px

list1=["ADANIPORTS", "ASIANPAINT","BAJAJ-AUTO","BAJFINSV","BPCL","CIPLA","DRREDDY","GAIL"]
data1=[]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
data_dict=[data1.append(i1) for i1 in list1]



def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

	html.Div([
	    html.Div([dcc.Dropdown(id="Stock_Chart_input1",options=[{'label': i, 'value': i} for i in data1])]),
	    html.Div([html.H1(id='stock_Name')]) ,
	    html.Div([dcc.Graph(id="Stock_Chart1")],style={'width': '50%', 'display': 'inline-block'}),
	    html.Div([dcc.Graph(id="Stock_Chart2")],style={'width': '50%', 'display': 'inline-block'}), 
      html.Div([dcc.Graph(id="Stock_Chart3")],style={'width': '50%', 'display': 'inline-block'}),     
      html.Div([dcc.Graph(id="Stock_Chart4")],style={'width': '50%', 'display': 'inline-block'}),                
	   	]),

])
   ###########################################################################start


@app.callback(dash.dependencies.Output("Stock_Chart1","figure"),
               [dash.dependencies.Input("Stock_Chart_input1", "value")]
               )
def update_fig1(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value+ ".NS.csv")
    return{
        "data":[go.Scatter(x=list(df['Date']),y=list(df['Close']),mode= 'lines')],
        #"layout":{"title": input_value}
    }



@app.callback(dash.dependencies.Output("Stock_Chart2","figure"),
               [dash.dependencies.Input("Stock_Chart_input1", "value")]
               )
def update_fig2(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value+ ".NS.csv")
    return{
        "data":[go.Scatter(x=list(df['Date']),y=list(df['Close']),mode= 'markers')],
    }



@app.callback(dash.dependencies.Output("Stock_Chart3","figure"),
               [dash.dependencies.Input("Stock_Chart_input1", "value")]
               )
def update_fig3(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value+ ".NS.csv")
    return{
        "data":[go.Candlestick(x=list(df['Date']),open=list(df['Open']),high=list(df['High']),low=list(df['Low']),close=list(df['Close']))],

    }


@app.callback(dash.dependencies.Output("Stock_Chart4","figure"),
               [dash.dependencies.Input("Stock_Chart_input1", "value")]
               )
def update_fig4(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value+ ".NS.csv")
    return{
        "data":[{'x': list(df['Date']), 'y': list(df['Close']) , 'type': 'bar'}],
    }



@app.callback(dash.dependencies.Output("stock_Name","children"),
               [dash.dependencies.Input("Stock_Chart_input1", "value")]
               )
def update_fig5(input_value):
    df=pd.read_csv("https://raw.githubusercontent.com/Selmer1990/Market_Prices_Dataset-Test-/master/"+ input_value+ ".NS.csv")
    return input_value

   ###########################################################################end

if __name__ == '__main__':
    app.run_server(port=4050)

#######