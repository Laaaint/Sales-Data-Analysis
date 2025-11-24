from dash import html, dcc, dash_table
from src.components.kpis import kpi_section, kpi_card
from src.components.filters import filter_section

def build_layout():
    layout = html.Div([
        html.H1('Amazon Sales Dashboard'),

        # Filtros
        filter_section(),

        # KPIs
        html.Div(
            id='kpi-row',
            children=[],
            style={
                'display': 'flex',
                'gap': '12px',
                'marginBottom': '12px'
            }
        ),

        # Gráficos principais
        html.Div([
            dcc.Graph(
                id='time-series',
                style={'width': '65%', 'display': 'inline-block'}
            ),
            html.Div([
                dcc.Graph(id='top-products'),
                dcc.Graph(id='price-dist')
            ],
            style={
                'width': '34%',
                'display': 'inline-block',
                'verticalAlign': 'top'
            })
        ]),

        # Mapa
        dcc.Graph(id='map-country', style={'height': '420px'}),

        # Tabela
        html.H3('Transações'),
        dash_table.DataTable(
            id='transactions-table',
            page_action='custom',
            page_current=0,
            page_size=10,
            columns=[
                {'name': c, 'id': c}
                for c in [
                    'order_id', 'order_date', 'product_title',
                    'category', 'price', 'quantity',
                    'revenue', 'country', 'rating'
                ]
            ]
        ),

        html.Div(
            id='footer',
            style={'marginTop': '12px', 'fontSize': '12px', 'color': 'gray'}
        )

    ], style={'padding': '18px'})

    return layout