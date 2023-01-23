import pandas as pd
from dash import Dash, html, dcc,dash_table
from dash.dependencies import Input, Output
import page1, page2, main
from components import Navbar
import  dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go




app = Dash(__name__,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.CYBORG],meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],)

nav = Navbar()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/':
        return main.layout

@app.callback(
    Output('bar', 'figure'),
    [Input('slider', 'value')])
def update_bar(year):

    dff = main.df[main.df['year']==year]
    fig1 = px.bar(dff, x='flow', y='trade_usd', template="plotly_dark")


    return fig1

@app.callback(
    Output('bar_1', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown3','value')])
def update_bar_1(year,com):

    dff = main.df[main.df['year']==year]
    if com:
        fig1 = px.bar(dff.query('commodity==%s' % com), x='commodity', y='trade_usd', template="plotly_dark")
    else:
        fig1 = px.bar(dff, x='commodity', y='trade_usd', template="plotly_dark")


    return fig1


@app.callback(
    Output('bar_2', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown2','value')])
def update_bar_2(year,cat):

    dff = main.df[main.df['year']==year]
    if cat:
        fig1 = px.bar(dff.query('category==%s' % cat), x='category', y='trade_usd', template="plotly_dark")
    else:
        fig1 = px.bar(dff, x='category', y='trade_usd', template="plotly_dark")


    return fig1

@app.callback(
    Output('scatter', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown1','value')])
def update_scatter(year,country):
    dff = main.df[main.df['year'] == year]
    if country:
        fig5 = px.scatter(dff.query("country_or_area==%s" % country), x="weight_kg", y="trade_usd", size="trade_usd", color="country_or_area", hover_name="country_or_area", log_x=True, size_max=60,template="plotly_dark")
    else:
        fig5 = px.scatter(dff, x="weight_kg", y="trade_usd", size="trade_usd", color="country_or_area",
                          hover_name="country_or_area", log_x=True, size_max=60, template="plotly_dark")
    return fig5

@app.callback(
    Output('line', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown1','value')])
def update_line(year,country):
    dff = main.df[main.df['year'] == year]
    if country:
        fig4 = px.line(dff.query("country_or_area==%s" % country), x="commodity", y="quantity", color='country_or_area',
                       template="plotly_dark")

    else:
        fig4 = px.line(dff, x="commodity", y="quantity", color='country_or_area',
                       template="plotly_dark")

    return fig4

@app.callback(
    Output('gauge_usd', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown1','value')])
def update_gauge_usd(year,country):
    dff = main.df[main.df['year'] == year]
    dff.fillna(0, inplace=True)
    if country:

        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff.query("country_or_area==%s" % country)['trade_usd']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': country[0] +" USD spent %d" % year, 'font': {'size': 24}},
            gauge={
            'axis': {'range': [0, sum(dff['trade_usd'])], 'tickwidth': 1, 'tickcolor': "black"},
            'bar': {'color': "green"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
            }}))
        fig6.update_layout(template='plotly_dark')
    else:
        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff['trade_usd']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Total USD spent %d" % year, 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, sum(dff['trade_usd'])], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "green"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                }}))
        fig6.update_layout(template='plotly_dark')

    return fig6

@app.callback(
    Output('gauge_kg', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown1','value')])
def update_gauge_kg(year,country):
    dff = main.df[main.df['year'] == year]
    dff.fillna(0, inplace=True)
    if country:

        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff.query("country_or_area==%s" % country)['weight_kg']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': country[0] +" Weight KG %d" % year, 'font': {'size': 24}},
            gauge={
            'axis': {'range': [0, sum(dff['weight_kg'])], 'tickwidth': 1, 'tickcolor': "black"},
            'bar': {'color': "red"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
            }}))
        fig6.update_layout(template='plotly_dark')
    else:
        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff['weight_kg']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Total weight Kg %d" % year, 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, sum(dff['weight_kg'])], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "red"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                }}))
        fig6.update_layout(template='plotly_dark')

    return fig6

@app.callback(
    Output('gauge_quantity', 'figure'),
    [Input('slider', 'value'),
     Input('dropdown1','value')])
def update_gauge_quantity(year,country):
    dff = main.df[main.df['year'] == year]
    dff.fillna(0,inplace=True)

    if country:

        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff.query("country_or_area==%s" % country)['quantity']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': country[0] +" Quantity %d" % year, 'font': {'size': 24}},
            gauge={
            'axis': {'range': [0, sum(dff['quantity'])], 'tickwidth': 1, 'tickcolor': "black"},
            'bar': {'color': "blue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
            }}))
        fig6.update_layout(template='plotly_dark')
    else:
        print(dff['quantity'])
        print(sum(dff['quantity']))
        fig6 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=sum(dff['quantity']),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Total Quantity %d" % year, 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, sum(dff['quantity'])], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "blue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                }}))
        fig6.update_layout(template='plotly_dark')

    return fig6

if __name__ == '__main__':
    app.run_server(debug=True)