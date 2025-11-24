import os
import pandas as pd
from typing import Optional

DATA_URL = os.environ.get('DATA_URL', '')
# LOCAL_SAMPLE = os.path.join('data', 'sample_amazon_sales.csv')
LOCAL_SAMPLE = r"C:\Users\Natália Rosa\Laaaint IO\Sales-Data-Analysis\data\sample_amazon_sales.csv"


def load_data(url: Optional[str] = None) -> pd.DataFrame:
    """
    Carrega um dataset CSV via URL ou arquivo local.
    Se a coluna 'order_date' não existir, cria uma automaticamente.
    """

    source = url or DATA_URL or LOCAL_SAMPLE

    # 1. Carregar CSV
    try:
        df = pd.read_csv(source)
    except Exception:
        df = pd.read_csv(LOCAL_SAMPLE)

    # 2. Garantir coluna order_date
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    else:
        # cria datas crescentes para evitar erro nos gráficos
        df['order_date'] = pd.date_range(
            start="2024-01-01",
            periods=len(df),
            freq="D"
        )

    # 3. Preço
    df['price'] = pd.to_numeric(df.get('price', 0), errors='coerce').fillna(0.0)

    # 4. Quantidade
    df['quantity'] = pd.to_numeric(df.get('quantity', 1), errors='coerce').fillna(1).astype(int)

    # 5. Rating
    df['rating'] = pd.to_numeric(df.get('rating', 0), errors='coerce').fillna(0.0)

    # 6. Receita
    df['revenue'] = df['price'] * df['quantity']

    return df