import sqlite3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read JSON data from file
def read_json_data():
    with open('products.json', 'r') as json_file:
        data = json.load(json_file)
    return data

# Function to read CSV data from file
def read_csv_data():
    data = []
    with open('products.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return data

# Function to read SQLite data from database
def read_sqlite_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': float(row[3])} for row in data]

# Route to display products based on source (json, csv, sql) and optional id parameter
@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    elif source == 'sql':
        data = read_sqlite_data()

    if id:
        filtered_products = [product for product in data if str(product['id']) == id]
        if not filtered_products:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        return render_template('product_display.html', products=filtered_products)
    else:
        return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)