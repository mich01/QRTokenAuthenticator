import io
import time
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import qrcode
from flask import request, make_response, jsonify, json, Response, send_file
from pip._vendor import requests
from pip._vendor.urllib3.util import url

from DBConnect import app
from Models.Members import Members, Certs
from Backend.Verifier import CryptoModule as CryptoMod

CryptoKey =app.config['SECRET_KEY']

@app.route('/verifymembership')
def verify():
    Response =''
    TokenString = request.args.get('CardKey')
    if TokenString:
        Data = CryptoMod.Decrypt(TokenString, CryptoKey)
        JsonData = SplitKeys(Data)
        Member = Members.query.filter(Members.MemberID == str(JsonData["MemberID"])).first()
        CertIDValidity = Certs.query.filter(Certs.CertID == str(JsonData["CertID"])).first()
        if Member and CertIDValidity:
            MemberID = Member.MemberID
            CertDate = CertIDValidity.Expires
            CurrentDate = datetime.today().date()
            if Member and CertIDValidity and CertDate > CurrentDate:
                Response = {"status":"Certificate is Valid","Names":Member.SurName+" "+Member.OtherNames,"Gender":Member.Gender,
                            "MembershipType":CertIDValidity.Description}
            elif CertIDValidity.MemberID != MemberID:
                Response = {"status":"Certificate doesnt belong to Member"}
            elif Member and CertIDValidity and CertDate < CurrentDate:
                Response = {"status":"Certificate has expired"}
        elif Member and not CertIDValidity:
            Response = {"status":"Member Found but Certificate Not Invalid"}
        else:
            Response ="Member Doesn't Exist"
    else:
        Response ="Empty Field"
    return jsonify({'Result':Response})

def SplitKeys(CardKey):
    Keys = CardKey.split(":")
    MemberValue = Keys[0].split("=")
    MemberID = MemberValue[1]
    CertValues = Keys[1].split("=")
    CertID =CertValues[1]
    return {"MemberID":MemberID,"CertID":CertID}

@app.route('/Generatekey')
def GenerateMemberCertKey():
    print("Function Called")
    MemberID = request.args.get('MemberID')
    CertID = request.args.get('CertID')
    MemberData = "MemberID="+MemberID+":"+"CertID="+CertID
    Result = CryptoMod.Encrypt(MemberData,CryptoKey).decode()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("https://<URL>/verifymembership?CardKey="+Result)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("/tmp/cert.png","PNG")
    response = send_file('/tmp/cert.png', attachment_filename='cert.png')
    return response
