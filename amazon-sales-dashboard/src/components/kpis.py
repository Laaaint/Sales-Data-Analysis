from dash import html

def kpi_card(title, value, subtitle=None):
    return html.Div([
    html.Div(title, style={'fontSize':'12px','color':'#6b7280'}),
    html.Div(value, style={'fontSize':'20px','fontWeight':'700'}),
    html.Div(subtitle or '', style={'fontSize':'11px','color':'#9ca3af'})
    ], style={'padding':'12px','borderRadius':'8px','backgroundColor':'#f3f4f6','flex':'1'})




def kpi_section(kpis):
# kpis: list of components
    return html.Div(kpis, style={'display':'flex','gap':'12px','marginBottom':'12px'})