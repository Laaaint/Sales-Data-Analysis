from dash import Input, Output, State
from app import app
import pandas as pd

from src import data_loader, preprocess
from src.components.charts import (
    time_series_fig,
    top_products_fig,
    price_dist_fig,
    map_fig
)
from src.components.kpis import kpi_card


@app.callback(
    Output('kpi-row', 'children'),
    Output('time-series', 'figure'),
    Output('top-products', 'figure'),
    Output('price-dist', 'figure'),
    Output('map-country', 'figure'),
    Output('transactions-table', 'data'),
    Input('load-url-btn', 'n_clicks'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date'),
    State('data-url-input', 'value'),
    State('transactions-table', 'page_current'),
    State('transactions-table', 'page_size')
)
def update_all(n_clicks, start_date, end_date, url, page_current, page_size):

    # carregar dados
    df = data_loader.load_data(url)
    df = preprocess.prepare(df)

    # filtros
    if start_date:
        df = df[df['order_date'] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df['order_date'] <= pd.to_datetime(end_date) + pd.Timedelta(days=1)]

    # KPIs
    total_revenue = df['revenue'].sum()
    total_orders = df['order_id'].nunique()
    ticket_avg = (total_revenue / total_orders) if total_orders else 0
    unique_products = df['product_id'].nunique()

    kpis = [
        kpi_card('Receita total', f'US$ {total_revenue:,.2f}'),
        kpi_card('Pedidos', f'{total_orders:,}'),
        kpi_card('Ticket médio', f'US$ {ticket_avg:,.2f}'),
        kpi_card('Produtos únicos', f'{unique_products:,}')
    ]

    # gráficos
    fig_ts = time_series_fig(df)
    fig_top = top_products_fig(df, top_n=10)
    fig_price = price_dist_fig(df)
    fig_map = map_fig(df)

    # tabela paginada
    dff = df.sort_values('order_date', ascending=False)
    start = page_current * page_size
    end = start + page_size

    table_data = dff[
        [
            'order_id',
            'order_date',
            'product_title',
            'category',
            'price',
            'quantity',
            'revenue',
            'country',
            'rating'
        ]
    ].iloc[start:end].to_dict('records')

    return kpis, fig_ts, fig_top, fig_price, fig_map, table_data
