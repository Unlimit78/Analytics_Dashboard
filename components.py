from dash import html
import dash_bootstrap_components as dbc

# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Tables", href="/page1")),
                dbc.NavItem(dbc.NavLink("Dashboard", href="/page2")),

            ] ,
            brand="Analytics Dashboard",
            brand_href="/",
            color="dark",
            dark=True,
        ),
    ])

    return layout