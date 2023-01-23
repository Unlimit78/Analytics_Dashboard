from dash import html,dcc,dash_table
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv('commodity_trade_statistics_data.csv')[:2000]


card_content1 = [
    dbc.CardBody(
        [
            html.H5("Tables", className="card-title"),

                dbc.NavItem(dbc.NavLink("Go tho the Tables", href="/page1")),

        ]
    ),
]
card_content2 = [
    dbc.CardBody(
        [
            html.H5("Dashboard", className="card-title"),

            dbc.NavItem(dbc.NavLink("Go to the Dashboard", href="/page2")),
        ]
    ),
]
card_content3 = [
    dbc.CardBody(
        [
            html.H5("References", className="card-title"),

            dbc.NavItem(dbc.NavLink("Go to the original dataset", href="https://www.kaggle.com/datasets/unitednations/global-commodity-trade-statistics?resource=download")),
        ]
    ),
]

layout = dbc.Container([
    dbc.Row(dbc.Col(html.H5("Welcome to this dashboard"))),
        dbc.Row(
            [
                dbc.Col([
                    html.P(["About Tables"]),
                    html.P([
                        "Main Table that represents all the data from current dataset."
                        "The Table that represents such statistics like min, max, count "
                        "for the value of trade_usd by year."
                        "The Table that represents such statistics like min, max, count "
                        "for the value of trade_usd by country."])
                ]),
                dbc.Col(dbc.Card(card_content1, color="danger", outline=True))

            ]
        ),
        dbc.Row(
            [
                dbc.Col([
                    html.P(["About Dashboard"]),
                    html.P([
                            "Charts that represent total usd, total weight, total quantity spent by the year by selected country."
                            "Bar charts that represent flow, commodity and category  by trade usd."
                            " Pie chart that represents quantity for each country."
                            "Scatter plot that represent weight by trade usd for every country. "
                            "Line chart that represent commodity by quantity  for every country."])
                ]),
                dbc.Col(dbc.Card(card_content2, color="danger", outline=True)),

            ]
        ),
        dbc.Row(
            [
                dbc.Col([
                    html.P(["About Dataset"]),
                    html.P([
                            "Are you curious about fertilizer use in developing economies?"
                            " The growth of Chinese steel exports? American chocolate consumption?"
                            " Which parts of the world still use typewriters?"
                            "You\'ll find all of that and more here. "
                            "This dataset covers import and export volumes for 5,000 commodities across most countries on Earth over the last 30 years."])
                ]),

                dbc.Col(dbc.Card(card_content3, color="danger", outline=True)),
            ]
        ),
])