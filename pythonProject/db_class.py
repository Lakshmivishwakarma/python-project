
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import uuid

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lakshmi@123'
app.config['MYSQL_DB'] = 'registration_details'

mysql = MySQL(app)


class UserDetails:
    def __init__(self, reg_id, username, email):
        self.reg_id = reg_id
        self.username = username
        self.email = email

    def save_to_db(self):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registered_data (RegistrationID , UserName, Email) VALUES (%s, %s, %s)",
                    (self.reg_id, self.username, self.email))
        mysql.connection.commit()
        cur.close()

    @classmethod
    def get_all_users(cls):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM registered_data")
        users = cur.fetchall()
        cur.close()
        return users

    @classmethod
    def delete_user(cls, reg_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM registered_data WHERE RegistrationID = %s", (reg_id,))
        mysql.connection.commit()
        cur.close()


# API endpoints
@app.route('/users', methods=['GET'])
def get_user():
    users = UserDetails.get_all_users()
    return jsonify({'users': users})


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    registration_id = str(uuid.uuid4())[:8]
    new_user = UserDetails(registration_id, username, email)
    new_user.save_to_db()
    return jsonify({'message': 'User added successfully'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(reg_id):
    UserDetails.delete_user(reg_id)
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

