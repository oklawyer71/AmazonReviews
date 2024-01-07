"""Instantiate a Dash app."""
import dash
from dash import dash_table
from dash import dcc
from dash import html

from flask import Flask

from .data import create_dataframe
from .layout import html_layout


def create_dashboard(app):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=app,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/css/dashcss.css',
        ]
    )

    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_module.index_string = html_layout

    # Create Layout
    dash_module.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {
                            "x": df["complaint_type"],
                            "text": df["complaint_type"],
                            "customdata": df["key"],
                            "name": "311 Calls by region.",
                            "type": "histogram",
                        }
                    ],
                    "layout": {
                        "title": "NYC 311 Calls category.",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_module.server


def create_data_table(df: DataFrame) -> DataTable:
    """
    Create Dash DataTable object from Pandas DataFrame.

    :param DataFrame df: Pandas DataFrame from which to build a Dash table.

    :returns: DataTable
    """
    table = DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
