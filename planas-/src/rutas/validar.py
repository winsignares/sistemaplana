from bd import db
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.validar import validar


routes_validar= Blueprint("routes_validar", __name__)




@routes_validar.route("/login", methods=["POST"])
def login():
  
    Ndocumento = request.json["Ndocumento"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(validar).filter(validar.Ndocumento == Ndocumento,validar.contraseña == contraseña,).first()

    # Busca el usuario en la base de datos
    if verificacion:
             
        return "a" 