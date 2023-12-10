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

    query = 'SELECT * FROM darahdarurat'
    cursor.execute(query)

    try:
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'id': row[0],
                'nama': row[1],
                'gol_darah': row[2],
                'deskripsi': row[3],
                'status': row[4],
                'tanggal':row[5]
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
    
def tambah_darah_darurat():
    
    data = request.get_json()
    
    nama = data['nama']
    gol_darah = data['gol_darah']
    deskripsi = data['deskripsi']
    
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        query = "INSERT INTO darahdarurat (nama, gol_darah, deskripsi, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nama, gol_darah, deskripsi, 'Terbuka'))
        conn.commit()

        response = {
            'status': 'success',
            'message': 'Data berhasil ditambahkan'
        }
        return jsonify(response)
    
    except Exception as e:
        conn.rollback()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat menambahkan data',
            'error': str(e)
        }
        return jsonify(response)
    
    finally:
        conn.close()