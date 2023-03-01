from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_city, get_opentime

def render(app):
    df = get_city()
    fig = px.bar(
            df,
            x=df.index,
            y="门店数量",
            title="星巴克门店数量TOP10",
            color="门店数量")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume")

def render1(app):
    df = get_opentime()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("open_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("index in @dropdown")
        fig = px.bar(
                filtered_data,
                x="city",
                y="city",
                title="城市门店开始营业数量")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume")
