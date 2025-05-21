# -*- coding: utf-8 -*-
"""
Created on Thu May 15 10:40:34 2025

@author: Afonso
"""

from flask import render_template, session
from classes.product import Product
from classes.stock import Stock
from datafile import filename
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64

def apps_plot():


    engine = create_engine(f'sqlite:///{filename}loja.db')
    
    # Load Stock table
    stock = pd.read_sql("SELECT product_id, level FROM Stock", engine)
    
    # Load Product table
    product = pd.read_sql("SELECT id, category FROM Product", engine)
    
    # Merge on product_id and id
    inventory = pd.merge(stock, product, left_on='product_id', right_on='id').drop(columns=['id'])
    
    # Group by category and sum level
    result = inventory.groupby('category', as_index=False)['level'].sum()
    result.rename(columns={'level': 'total_stock'}, inplace=True)
    
    # Set 'category' as index for proper x-axis labels
    result.set_index('category', inplace=True)
    
    # Plot the data
    fig, ax = plt.subplots()
    result.plot(kind='bar', ax=ax, color='lightgreen', legend=False)
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Number of Products")
    ax.set_title("Number of Products by Category")
    plt.xticks(rotation=45)
    
    # Save to buffer
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)


    image = base64.b64encode(buf.getvalue()).decode('utf-8')
    return render_template("plot.html", image=image, ulogin=session.get("user"))
