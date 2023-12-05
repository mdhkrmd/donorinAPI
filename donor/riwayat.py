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

def riwayat_donor():
    nik = request.args.get('nik')

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    query = "SELECT * FROM daftardonor WHERE nik = '" + nik + "'"
    cursor.execute(query)
    
    try:
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'nik': row[1],
                'nama': row[2],
                'darah': row[3],
                'alamat': row[4],
                'no': row[5],
                'lokasi': row[6],
                'jadwal': row[7],
                'status': row[8],
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