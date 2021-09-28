from flask import jsonify
from DBConnect import app

# handle login failed
@app.errorhandler(401)
def login_failed(e):
    return jsonify({ 'error': "Login Failed" })


# handle Unkown Path
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({ 'error': "invalid request" })

# forbiden Pages
@app.errorhandler(403)
def forbidden(e):
    return jsonify({ 'error': "Forbidden" })

