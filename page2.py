from dash import html,dcc,dash_table
import dash_bootstrap_components as dbc
from main import df
import plotly.express as px
import plotly.graph_objects as go




fig2 = px.pie(df.query("year==2016"), values='quantity', names='country_or_area',template="plotly_dark" )


layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                html.P(["Country"]),
                dcc.Dropdown(df['country_or_area'].unique(), multi=True,id='dropdown1'),
            ]),
            dbc.Col([
                html.P(["Category"]),
                dcc.Dropdown(df['category'].unique(), multi=True, id='dropdown2'

            )]),
            dbc.Col([
                html.P(["Commodity"]),
                dcc.Dropdown(df['commodity'].unique(), multi=True,id='dropdown3'
            )])
    ]),

        dbc.Row([
                html.P(["Time Picker"]),
                dcc.Slider(min(df['year'].unique()),max(df['year'].unique()),1,id="slider",value=max(df['year'].unique()),
                        marks={str(year): str(year) for year in df['year'].unique()}
               ),
        ],className="slider"),

        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="gauge_usd",animate=True)
                ),
                dbc.Col(
                    dcc.Graph(id="gauge_kg",animate=True)
                ),
                dbc.Col(
                    dcc.Graph(id="gauge_quantity",animate=True)
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="bar",animate=True,),width=3
                ),
                dbc.Col(
                    dcc.Graph(id="bar_2",animate=True),width=3
                ),
                dbc.Col(
                    dcc.Graph(id="bar_1",animate=True)
                ),
            ]
        ),
        dbc.Row(
            [
            dbc.Col(
                    dcc.Graph(figure=fig2,id="piechart",animate=True),width=4
                ),
            dbc.Col(
                    dcc.Graph(id="scatter",animate=True,)
                ),

        ]
        ),
        dbc.Row(
            [

            dbc.Col(
                    dcc.Graph(id="line",animate=True,)
                ),

        ]
        ),

])