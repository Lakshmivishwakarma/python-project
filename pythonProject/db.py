from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from schema import ProductSchema, UpdateProductSchema

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lakshmi@123'
app.config['MYSQL_DB'] = 'inventory'
mysql = MySQL(app)

product_schema = ProductSchema()
update_product_schema = UpdateProductSchema()


class Product:
    def __init__(self, product_name, display_name, selling_price,
                 mrp, quantity, product_weight, measuring_unit,
                 expiry_date):
        self.product_name = product_name
        self.display_name = display_name
        self.selling_price = selling_price
        self.mrp = mrp
        self.quantity = quantity
        self.product_weight = product_weight
        self.measuring_unit = measuring_unit
        self.expiry_date = expiry_date


class Inventory:
    @staticmethod
    def add_inventory(data):
        product = Product(
            product_name=data.get('product_name'),
            display_name=data.get('display_name'),
            selling_price=data.get('selling_price'),
            mrp=data.get('mrp'),
            quantity=data.get('quantity'),
            product_weight=data.get('product_weight'),
            measuring_unit=data.get('measuring_unit'),
            expiry_date=data.get('expiry_date')
        )

        errors = product_schema.validate(product.__dict__)
        if errors:
            return jsonify({"error": errors})

        cur = mysql.connection.cursor()
        # cur.execute(
        #     "INSERT INTO student_details (RollNo, FirstName, MiddleName, LastName, Dob, Class, Address, City, State, Pincode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        #     (request_data.rollNo, request_data.firstName, request_data.middlename, request_data.lastName,
        #      request_data.dob, request_data.classSection, request_data.address,
        #      request_data.city, request_data.state, request_data.pincode))

        cur.execute("INSERT INTO product (product_name, display_name, selling_price, mrp, quantity, product_weight, "
                    "measuring_unit, expiry_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (product.product_name, product.display_name, product.selling_price, product.mrp,
                     product.quantity, product.product_weight, product.measuring_unit, product.expiry_date))
        mysql.connection.commit()
        cur.execute("SELECT * FROM product WHERE id = LAST_INSERT_ID()")
        added_data = cur.fetchone()
        cur.close()
        return jsonify(added_data)

    @staticmethod
    def remove_inventory(product_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, is_deleted FROM product WHERE id = %s", (product_id,))
        result = cur.fetchone()
        if result is None:
            cur.close()
            return "Product with the specified ID does not exist", 404
        if result[1] == 1:
            cur.close()
            return "Product with the specified ID is already deleted", 400

        cur.execute("UPDATE product SET is_deleted = 1 WHERE id = %s", (product_id,))
        mysql.connection.commit()
        cur.close()
        return "Product removed successfully", 200

    @staticmethod
    def get_inventory(product_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM product WHERE id = %s AND is_deleted = 0", (product_id,))
        item = cur.fetchone()
        cur.close()
        if item is None:
            return "Item does not exist in database", 404
        return item, 200

    @staticmethod
    def add_inventory_quantity(product_id, data):
        product_count = data.get('quantity')
        errors = update_product_schema.validate(product_count)
        if errors:
            return jsonify({"error": errors})

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, quantity, is_deleted, product_name FROM product WHERE id = %s", (product_id,))
        result = cur.fetchone()
        if not result:
            cur.close()
            return "Product ID not found in the database", 404
        elif result[2] == 1:
            cur.close()
            return "This product has been deleted", 400
        else:
            updated_count = int(result[1]) + int(product_count)

            cur.execute("UPDATE product SET quantity = %s WHERE id = %s", (updated_count, product_id))
            mysql.connection.commit()
            cur.close()
            return f"New count for product {result[3]} is {updated_count}", 200


inventory = Inventory()


@app.route('/product_service/inventory/<int:product_id>', methods=["GET"])
def get_item(product_id):
    result, status_code = inventory.get_inventory(product_id)
    return jsonify(result)


@app.route('/product_service/inventory', methods=["POST"])
def add_item():
    data = request.json
    result = inventory.add_inventory(data)
    return result


@app.route('/product_service/inventory/<int:product_id>', methods=["DELETE"])
def delete_item(product_id):
    result = inventory.remove_inventory(product_id)
    return jsonify(result)


@app.route('/product_service/inventory/<int:product_id>', methods=["PUT"])
def update_item(product_id):
    data = request.json
    result = inventory.add_inventory_quantity(product_id, data)
    return result


if __name__ == '__main__':
    app.run(debug=True)
