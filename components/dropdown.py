from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_opentime

def render(app):
    list_open = get_opentime()
    all_open = [{'label':i,'value':i} for i in list_open]
    @app.callback(
    Output(component_id='open_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_all_open(n):
        return list_open

    return html.Div(
        children=[
            html.H6("开始营业时间选择"),
            dcc.Dropdown(
                options=all_open,
                multi=True,
                id = "open_dropdown",
                value= 1
            ),
            dbc.Button(
                children=["选择所有选项"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )