import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

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
df = px.data.gapminder().query("country=='Canada'")
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div([
	    dcc.Graph(
	        id='example-graph1',
	        figure={
	            'data': [
	                go.Pie(labels = ['C', 'C++', 'Java', 'Python', 'PHP'] , values = [23,17,35,29,12]),

	            ],
	            'layout': {
	                'title': 'Pie Chart'
	            }
	        }
	    ),
    ],style={'width': '25%', 'display': 'inline-block'}),

    html.Div([    
	    dcc.Graph(
	        id='example-graph2',
	        figure={
	            'data': [
	                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
	                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
	            ],
	            'layout': {
	                'title': 'Bar Chart'
	            }
	        }
	    )
	],style={'width': '25%', 'display': 'inline-block'}),

    html.Div([    

	    dcc.Graph(
	        id='example-graph3',
	        figure={
	            'data': [
	                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'Line', 'name': 'SF'},
	            ],
	            'layout': {
	                'title': 'Line Chart'
	            }
	        }
	    )
	],style={'width': '25%', 'display': 'inline-block'}),

    html.Div([   
	    dcc.Graph(
	        id='example-graph4',
	        figure={
	            'data': [
						go.Scatter( x = [8.86, 15.35, 21.97, 29.76, 39.29, 53.67, 64.63], y = [1951,1961,1971,1981,1991,2001, 2011],  marker = dict(color = "crimson", size = 12),   mode = "markers", name = "Women"),
	            ],
	            'layout': {
	                'title': 'Line Chart'
	            }
	        }
	    )
	],style={'width': '25%', 'display': 'inline-block'}),

	 html.Div(children=[
	    html.H4(children='US Agriculture Exports (2011)'),
	    generate_table(df)
	],style={'width': '100%', 'display': 'inline-block'})		
])

if __name__ == '__main__':
    app.run_server(debug=True)