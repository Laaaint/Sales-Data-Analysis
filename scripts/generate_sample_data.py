# scripts/generate_sample_data.py
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

OUT = os.path.join('data', 'sample_amazon_sales.csv')

def generate(n=3000):
    rng = np.random.default_rng(42)
    categories = ['Electronics','Toys','Books','Home','Beauty','Clothing']
    products = {
        'Electronics': ['Echo Dot','Fire TV Stick','Kindle','USB-C Cable'],
        'Toys': ['Lego','Plush','Board Game'],
        'Books': ['Python 101','Data Science','Novel'],
        'Home': ['Vacuum','Air Fryer','Lamp'],
        'Beauty': ['Moisturizer','Sunscreen'],
        'Clothing': ['T-Shirt','Jeans','Sneakers']
    }
    rows = []
    start = datetime.now() - timedelta(days=180)
    for i in range(n):
        cat = rng.choice(categories)
        prod = rng.choice(products[cat])
        price = round(abs(rng.normal(30 if cat!='Electronics' else 80, 20)) + 1, 2)
        qty = int(rng.integers(1,5))
        rows.append({
            'order_id': f'ORD{i+1000}',
            'order_date': (start + timedelta(days=int(rng.integers(0,180)))).isoformat(),
            'product_id': f'P{rng.integers(1000,9999)}',
            'product_title': prod,
            'category': cat,
            'price': price,
            'quantity': qty,
            'country': rng.choice(['US','GB','CA','DE','FR','BR','IN','JP']),
            'rating': round(rng.uniform(1.0,5.0),1)
        })
    df = pd.DataFrame(rows)
    os.makedirs('data', exist_ok=True)
    df.to_csv(OUT, index=False)
    print('Gerado:', OUT)

if __name__ == '__main__':
    generate(4000)
