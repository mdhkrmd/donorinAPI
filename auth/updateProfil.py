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

def updateProfil():
    data = request.get_json()
    nik = data['nik']
    nama = data['nama']
    lahir = data['lahir']
    darah = data['darah']
    alamat = data['alamat']
    no = data['no']

    # Koneksi MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE nik = %s", (nik,))
        result = cursor.fetchone()

        if not result:
            conn.close()
            response = {
                'status': 'error',
                'message': 'NIK tidak terdaftar'
            }
            return jsonify(response)

        else:
            query = """
                        UPDATE users 
                        SET 
                            `nama` = %s,
                            `lahir` = %s,
                            `darah` = %s,
                            `alamat` = %s,
                            `nohp` = %s
                        WHERE `nik` = %s
                    """
            cursor.execute(query, (nama, lahir, darah, alamat, no, nik))
            conn.commit()
            conn.close()

            response = {
                'status': 'success',
                'message': 'Berhasil ganti data'
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