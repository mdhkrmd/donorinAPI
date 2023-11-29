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
def showUsers():
    username_id = request.args.get('username')
    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    if username_id is None:
        query = "SELECT * FROM users"
    else:
        query = "SELECT * FROM users WHERE username = '" + username_id + "'"
    
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'username': row[1],
                'password': row[2],
                'nik': row[3],
                'nama': row[4],
                'lahir': row[5],
                'darah': row[6],
                'alamat': row[7],
                'nohp': row[8],
                'poin': row[9]
            }
            results.append(result)

        return jsonify(results)

    except Exception as e:
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat mengambil data',
            'error': str(e)
        }
        return jsonify(response)

def register():
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    nik = data['nik']
    nama = data['nama']
    lahir = data['lahir']
    darah = data['darah']
    alamat = data['alamat']
    nohp = data['nohp']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'Username sudah terdaftar'
            }
            return jsonify(response)

        cursor.execute("INSERT INTO users (username, password, nik, nama, lahir, darah, alamat, nohp, poin) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)", 
                       (username, password, nik, nama, lahir, darah, alamat, nohp, 100))
        conn.commit()
        conn.close()

        response = {
            'status': 'success',
            'message': 'Akun berhasil dibuat'
        }

        return jsonify(response)
    except Exception as e:
        conn.rollback()
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat membuat akun',
            'error': str(e)
        }
        return jsonify(response)