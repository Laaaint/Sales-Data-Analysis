from dash import dcc
import plotly.express as px

def time_series_fig(df):
    ts = df.set_index('order_date').resample('D').agg({'revenue':'sum'}).reset_index()
    fig = px.line(ts, x='order_date', y='revenue', title='Receita por dia')
    return fig

def top_products_fig(df, top_n=10):
    top = df.groupby('product_title').agg({'revenue':'sum'}).reset_index().sort_values('revenue', ascending=False).head(top_n)
    fig = px.bar(top, x='revenue', y='product_title', orientation='h', title=f'Top {top_n} produtos')
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig

def price_dist_fig(df):
    fig = px.histogram(df, x='price', nbins=30, title='Distribuição de preços')
    return fig

def map_fig(df):
    agg = df.groupby('country').agg({'revenue':'sum'}).reset_index()
# assume ISO codes or country names; Plotly tentará mapear
    fig = px.choropleth(agg, locations='country', color='revenue', title='Receita por país', hover_data=['revenue'])