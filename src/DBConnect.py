from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify



# connection code
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)

#Connection Parameters
app.config["SQLALCHEMY_DATABASE_URI"] = '<URL_CONNECTION_PARAMS_TO_DB>'
app.secret_key = bytes('<SECRET_KEY>', 'utf-8')


#instatiate the db model
db=SQLAlchemy(app)