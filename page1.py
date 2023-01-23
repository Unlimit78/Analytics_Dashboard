from dash import html,dcc,dash_table
import dash_bootstrap_components as dbc
from main import df

dff = df.copy()


df1 = dff.groupby('year')['trade_usd'].agg(['min','max','count']).reset_index()
df1 = df1[['year','min','max','count']].copy()

df2 = dff.groupby('country_or_area')['trade_usd'].agg(['min','max','count']).reset_index()
df2 = df2[['country_or_area','min','max','count']].copy()

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
    html.P(["General Table"]),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],

        style_header={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid red'

        },
        style_data={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid red'
        },
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    dbc.Row([

            dbc.Col([
                html.P(["General statistic by year"]),
                dash_table.DataTable(
                    data=df1.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df1.columns],
                    style_header={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid green'

        },
                    style_data={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid green'
        },
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current= 0,
                    page_size= 10,
                )
            ]),
            dbc.Col([
                html.P(["General statistic by country"]),
                dash_table.DataTable(
                    data=df2.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df2.columns],
                    style_header={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid blue'

        },
                    style_data={
            'backgroundColor': 'rgb(0, 0, 0)',
            'color': 'white',
            'border': '1px solid blue'
        },
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current= 0,
                    page_size= 10,
                )
            ])
    ]),
])