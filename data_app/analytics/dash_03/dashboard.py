from dash import Dash
import dash_bootstrap_components as dbc
from .etl import Etl
from .layout import create_layout
from .callbacks import update_charts
from dash.dependencies import Input, Output
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Create an instance of the Etl class
etl_instance = Etl()


def create_dashboard_03(server):
    dash_app3 = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server, url_base_pathname='/dashboard3/')
    
    # Set the layout
    dash_app3.layout = create_layout()

    # Callbacks
    @dash_app3.callback(
        [Output('tree_map', 'figure'),
        Output('map_state', 'figure'),
        Output('table', 'columns'),
        Output('table', 'data'),
        Output('barchart', 'figure'),
        Output('barchart_tkm', 'figure'),
        Output('lineplot_revenue', 'figure'),
        Output('lineplot_grow_up', 'figure'),],
        [Input('filter_axis', 'value')])
    def charts(filter_axis):
        return update_charts(filter_axis)

    return dash_app3


