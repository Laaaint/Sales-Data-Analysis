import pandas as pd


def prepare(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformações e features comuns ao dashboard.
    - normaliza nomes de colunas
    - limpa nulos
    - cria 'year', 'month', 'day'
    """
    df = df.copy()

    # normaliza colunas
    df.columns = [c.strip() for c in df.columns]

    # colunas esperadas, garantir presença
    expected = [
        'order_id', 'order_date', 'product_id', 'product_title', 'category',
        'price', 'quantity', 'country', 'rating', 'revenue'
    ]

    for col in expected:
        if col not in df.columns:
            df[col] = None

    # limpar alguns nulos
    df['product_title'] = df['product_title'].fillna('Unknown')
    df['category'] = df['category'].fillna('Other')
    df['country'] = df['country'].fillna('US')

    # tipos
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(1).astype(int)
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0.0)

    # receita
    df['revenue'] = df['price'] * df['quantity']

    # datetimes
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['day'] = df['order_date'].dt.date

    return df