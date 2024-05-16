# from flask import Flask
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# # Required
# app.config["MYSQL_USER"] = "user"
# app.config["MYSQL_PASSWORD"] = "password"
# app.config["MYSQL_DB"] = "database"
# # Extra configs, optional:
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes
#
# mysql = MySQL(app)
#
# class Inventory:
#     # def add_product(self, product_name, product_count):
#     #     if product_name not in self.product_inventory:
#     #         self.product_inventory[product_name] = product_count
#     #         print(self.product_inventory)
#     #     else:
#     #         print("The product is already in inventory")
#     #
#     # def increase_prod_count(self, product_name, product_count):
#     #     if product_name in self.product_inventory:
#     #         self.product_inventory[product_name] += product_count
#     #         print(self.product_inventory)
#     #     else:
#     #         print("The product is not available in inventory")
#     #
#     # def decrease_prod_count(self, product_name, count):
#     #     if product_name in self.product_inventory:
#     #         if self.product_inventory[product_name] >= count:
#     #             self.product_inventory[product_name] -= count
#     #             print(self.product_inventory)
#     #         else:
#     #             print("count will not be greater then remaining product count")
#     #
#     # def remove_product(self, product_name):
#     #     if product_name in self.product_inventory:
#     #         del (self.product_inventory[product_name])
#     #         return True
#     #     else:
#     #         return False
#
#     def get_inventory_list(self):
#         products = Product.query.all()
#         inventory_list = [{"name": product.name, "count": product.count} for product in products]
#         # return jsonify(inventory_list)
#         return "success"
#
#
# mobile_inventory = Inventory()
#
# @app.route('/inventory', methods=["GET"])
# def get_inventory():
#     return mobile_inventory.get_inventory_list()
#
# #
# # @app.route('/inventory', methods=["POST"])
# # def add_inventory():
# #     name = request.form['product_name']
# #     count = int(request.form['count'])
# #     mobile_inventory.add_product(name, count)
# #     return jsonify(mobile_inventory.product_inventory)
# #
# #
# # @app.route('/inventory/<product_name>', methods=["DELETE"])
# # def delete_product(product_name):
# #     res_result = mobile_inventory.remove_product(product_name)
# #
# #     if res_result:
# #         return jsonify(mobile_inventory.product_inventory)
# #     else:
# #         return "The product is not available in inventory"
# #     # return jsonify(mobile_inventory.dict)
# #
# #
# # @app.route('/inventory/<product_name>', methods=["PUT"])
# # def update_product_count(product_name):
# #     count = int(request.form['count'])
# #     mobile_inventory.increase_prod_count(product_name, count)
# #     # print("The" ,product_name, "is increased by", count)
# #     return jsonify(mobile_inventory.product_inventory)
#
#
# print(mobile_inventory)
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

# product_name
# display_name
# selling_price
# mrp
# quantity
# product_weight
# measuring_unit
# expiry_date
# is_deleted
# class product:
# class Product:
#     def __init__(self, product_name, count, model, brand, color, price, storage):
#         self.product_name = product_name
#         self.count = count
#         self.model = model
#         self.brand = brand
#         self.color = color
#         self.price = price
#         self.storage = storage

