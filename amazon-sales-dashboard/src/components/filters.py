from dash import html, dcc

def filter_section():
    return html.Div([
    dcc.DatePickerRange(id='date-range'),
    dcc.Dropdown(id='category-filter', multi=True, placeholder='Categoria', style={'width':'220px','marginLeft':'8px'}),
    dcc.Dropdown(id='country-filter', multi=True, placeholder='País', style={'width':'140px','marginLeft':'8px'}),
    dcc.Input(id='data-url-input', type='text', placeholder='URL CSV (opcional)', style={'width':'350px','marginLeft':'8px'}),
    html.Button('Carregar', id='load-url-btn', n_clicks=0, style={'marginLeft':'8px'})
    ], style={'display':'flex','alignItems':'center','gap':'8px','marginBottom':'12px'})