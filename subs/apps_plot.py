# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:40:34 2025

@author: Afonso
"""

from flask import render_template, session, request, jsonify
from classes.product import Product
from classes.stock import Stock
from classes.store import Store
from datafile import filename
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def generate_plot(store=None):
    engine = create_engine(f'sqlite:///{filename}loja.db')

    stock = pd.read_sql("SELECT product_id, level, store_id FROM Stock", engine)
    if store:
        stock = stock[stock['store_id'] == int(store)]

    product = pd.read_sql("SELECT id, category FROM Product", engine)
    inventory = pd.merge(stock, product, left_on='product_id', right_on='id').drop(columns=['id'])

    result = inventory.groupby('category', as_index=False)['level'].sum()
    result.rename(columns={'level': 'total_stock'}, inplace=True)
    result.set_index('category', inplace=True)

    fig, ax = plt.subplots()
    result.plot(kind='bar', ax=ax, color='lightgreen', legend=False)
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Number of Products")
    ax.set_title("Number of Products by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return base64.b64encode(buf.getvalue()).decode('utf-8')

def apps_plot():
    engine = create_engine(f'sqlite:///{filename}loja.db')
    stores = pd.read_sql("SELECT DISTINCT store_id FROM Stock", engine)['store_id'].tolist()
    image = generate_plot()
    return render_template("plot.html", image=image, stores=stores, ulogin=session.get("user"))

def apps_update_plot():
    store = request.json.get("store")
    image = generate_plot(store)
    return jsonify({"image": image})