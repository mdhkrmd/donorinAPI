import os
from flask import Flask
from auth.register import register, showUsers
from auth.login import login
from auth.forgot import forgot
from donor.daftar import daftar_donor
from rspmi.show import get_rspmi, get_rspmi_detail
from darahDarurat.index import get_darah_darurat

app = Flask(__name__,static_folder='assets', template_folder='web')

#=============================================================================
# Auth
@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/register', methods=['POST'])
def register_route():
    return register()

@app.route('/users', methods=['GET'])
def showUsers_route():
    return showUsers()

@app.route('/forgot', methods=['POST'])
def forgot_route():
    return forgot()

#=============================================================================
# Donor
@app.route('/daftar', methods=['POST'])
def daftar_route():
    return daftar_donor()

#=============================================================================
# RSPMI
@app.route('/rspmi', methods=['GET'])
def get_rspmi_route():
    return get_rspmi()

@app.route('/rspmi/detail', methods=['GET'])
def get_rspmi_detail_route():
    return get_rspmi_detail()

# Darah Darurat
@app.route("/darah-darurat", methods=["GET"])
def get_darah_darurat_route():
    return get_darah_darurat()
    
if __name__ == '__main__':
    # Mengatur kredensial Google Cloud jika diperlukan
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth/key.json"

    # Menjalankan aplikasi di localhost pada port 8080
    app.run(host="localhost", port=8080)