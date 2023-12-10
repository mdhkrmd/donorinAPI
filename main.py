import os
from flask import Flask
from auth.register import register, showUsers
from auth.login import login
from auth.forgot import forgot
from auth.updateProfil import updateProfil
from donor.daftar import daftar_donor, daftar_donor_darurat
from donor.darahDarurat import get_darah_darurat, tambah_darah_darurat
from donor.riwayat import riwayat_donor
from rspmi.show import get_rspmi, get_rspmi_detail
from artikel.artikel import get_artikel

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

@app.route('/updateprofil', methods=['POST'])
def update_route():
    return updateProfil()

#=============================================================================
# Donor
@app.route('/daftar', methods=['POST'])
def daftar_route():
    return daftar_donor()

@app.route('/darah-darurat', methods=['GET'])
def get_darah_darurat_route():
    return get_darah_darurat()

@app.route('/riwayat', methods=['GET'])
def get_riwayat_route():
    return riwayat_donor()

@app.route('/tambah-darah-darurat', methods=['POST'])
def tambah_darah_darurat_route():
    return tambah_darah_darurat()

@app.route('/daftar-donor-darurat', methods=['POST'])
def daftar_donor_darurat_route():
    return daftar_donor_darurat()

#=============================================================================
# RSPMI
@app.route('/rspmi', methods=['GET'])
def get_rspmi_route():
    return get_rspmi()

@app.route('/rspmi/detail', methods=['GET'])
def get_rspmi_detail_route():
    return get_rspmi_detail()

#=============================================================================
# RSPMI
@app.route('/artikel', methods=['GET'])
def get_artikel_route():
    return get_artikel()
    
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth/key.json" 
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))