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

def get_darah_darurat():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = 'SELECT id, nama, gol_darah, deskripsi FROM darahdarurat'
    cursor.execute(query)

    try:
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'nama': row[1],
                'gol_darah': row[2],
                'deskripsi': row[3]
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