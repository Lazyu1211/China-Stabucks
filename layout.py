from dash import Dash,html
import dash_bootstrap_components as dbc
from components import scatter_charts, bar_charts, dropdown

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5bDrnQ1PeohVWyxX_KLYR1M510V9nm2o2Dd-F1EsMuQNz12sLdKpsgtaTlpaHQJdm7tw&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCa5UHiHcLxnjvEObaHv5SzVQtw41pOUflfA&usqp=CAU"

def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.P(children="✨✨✨✨✨✨✨✨✨", className="header-emoji"),
        html.H1(
                "中国地区星巴克门店分析", className="header-title"
              ),
        html.P(
                "基于中国地区星巴克门店的数据对于门店位置以及策略的分析!!!🔥🔥🔥✨✨✨",
                className="header-description",
                ),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        dropdown.render(app),
        dropdown.render1(app)
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(bar_charts.render1(app),lg=6),
            dbc.Col(bar_charts.render2(app),lg=6),
            dbc.Col(scatter_charts.render(app),lg=12),
            dbc.Col(bar_charts.render(app),lg=12)
        ],className="mt-4")
    ])
