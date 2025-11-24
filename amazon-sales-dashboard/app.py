# app.py
from dash import Dash
from src.layout import build_layout
import os

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Build layout and register callbacks
app.layout = build_layout()

# register callbacks after layout is created
from src import callbacks   # noqa: E402,F401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run(debug=True, port=port)
