import os
from flask import Flask
from auth.register import register, showUsers
from auth.login import login
from auth.forgot import forgot
from donor.daftar import daftar_donor

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

    
if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "auth/key.json" 
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))