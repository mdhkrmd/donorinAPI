from flask import Flask, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# Konfigurasi koneksi MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'zDEqSAF-8<vMva-('
app.config['MYSQL_DATABASE_DB'] = 'donorin'
app.config['MYSQL_DATABASE_HOST'] = '34.128.101.207'

mysql.init_app(app)

def forgot():
    data = request.get_json()
    username = data['username']
    new_password = data['new_password']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'Username tidak terdaftar'
            }
            return jsonify(response)

        else:
            query = "UPDATE users SET `password` = '" + new_password + "' WHERE `username` = '" + username + "'"
            cursor.execute(query)
            conn.commit()
            conn.close()

            response = {
                'status': 'success',
                'message': 'Berhasil ganti password'
            }

            return jsonify(response)
    except Exception as e:
        conn.rollback()
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan',
            'error': str(e)
        }
        return jsonify(response)