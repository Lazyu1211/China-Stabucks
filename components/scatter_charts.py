from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_data


def render(app):
    df = get_data()
    fig = px.scatter(
            df, 
            x="longitude", 
            y="latitude",
            title="星巴克门店经纬度分布",
            color="hasArtwork",
            size="hasArtwork")
    return html.Div(dcc.Graph(figure=fig), id="scatter")