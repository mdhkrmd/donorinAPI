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

def daftar_donor():
    data = request.get_json()
    
    nik = data['nik']
    nama = data['nama']
    darah = data['darah']
    alamat = data['alamat']
    nohp = data['nohp']
    lokasi = data['lokasi']
    jadwal = data['jadwal']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO daftardonor (nik, nama, darah, alamat, no, lokasi, jadwal, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (nik, nama, darah, alamat, nohp, lokasi, jadwal, 'Antrian'))
        conn.commit()
        conn.close()

        response = {
            'status': 'success',
            'message': 'Pendaftaran berhasil dibuat'
        }

        return jsonify(response)
    except Exception as e:
        conn.rollback()
        conn.close()
        response = {
            'status': 'error',
            'message': 'Terjadi kesalahan saat pendaftaran',
            'error': str(e)
        }
        return jsonify(response)