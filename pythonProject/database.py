from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask import jsonify
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lakshmi@123'
app.config['MYSQL_DB'] = 'inventory'
mysql = MySQL(app)


@app.route('/inventory')
def get_inventory():
    cur = mysql.connection.cursor()
    cur.execute("SELECT productname, count FROM product")
    data = cur.fetchall()
    inventory = {row[0]: row[1] for row in data}
    cur.close()
    return jsonify(inventory)


@app.route('/inventory', methods=["POST"])
def add_inventory():
    name = request.form['product_name']
    count = int(request.form['count'])
    cur = mysql.connection.cursor()
    cur.execute("SELECT count FROM product WHERE productname = %s", (name,))
    existing_count = cur.fetchone()
    if existing_count:
        new_count = existing_count[0] + count
        cur.execute("UPDATE product SET count = %s WHERE productname = %s", (new_count, name))
    else:
        cur.execute("INSERT INTO product (productname, count) VALUES (%s, %s)", (name, count))

    mysql.connection.commit()
    cur.close()
    return 'Success'


@app.route('/inventory/<product_name>', methods=["DELETE"])
def delete_product(product_name):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product WHERE productname = %s", (product_name,))
    mysql.connection.commit()
    cur.close()
    return f'{product_name} has been deleted'


@app.route('/inventory/<product_name>', methods=["PUT"])
def update_product(product_name):
    count = int(request.form['count'])
    cur = mysql.connection.cursor()
    cur.execute("UPDATE product SET count = %s WHERE productname = %s", (count, product_name))
    mysql.connection.commit()
    cur.close()
    return f'The {product_name} count is updated to {count}'


if __name__ == '__main__':
    app.run(debug=True)
