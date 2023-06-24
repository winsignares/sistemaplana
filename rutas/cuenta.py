from bd import db
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.validar import validar


routes_cuenta = Blueprint("routes_cuenta", __name__)



@routes_cuenta.route('/perfil',methods=['POST'])
def cuenta():

    nombre= request.form['nombre']
    correo= request.form['correo']
    clave= request.form['clave']  

    new_section = validar(nombre, correo, clave )
    db.session.add(new_section)
    db.session.commit()
    return "ok"