from dash import Dash,html
import dash_bootstrap_components as dbc
from layout import create_layout

def main():
    app = Dash(external_stylesheets=[dbc.themes.QUARTZ])
    app.title = "中国地区星巴克门店分析"
    app.layout = create_layout(app)
    app.run_server(debug=True)

if __name__ == "__main__":
   main()