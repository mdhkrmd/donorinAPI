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

def get_rspmi():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = 'SELECT * FROM rspmi'
    cursor.execute(query)

    try:
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'nama': row[1],
                'alamat': row[2],
                'deskripsi': row[3],
                'foto': row[4]
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


def get_rspmi_detail():
    product_id = request.args.get('id')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT * FROM rspmi WHERE id = '" + product_id + "'"
    cursor.execute(query)
    
    try:
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'nama': row[1],
                'alamat': row[2],
                'deskripsi': row[3],
                'foto': row[4]
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