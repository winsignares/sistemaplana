from bd import db
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.registro import registross


routes_formulario = Blueprint("routes_section", __name__)



@routes_formulario.route('/guardar',methods=['POST'])
def saveSection():
    
    nombre= request.form['nombre']
    Apellido= request.form['apellido']
    Curso= request.form['curso'] 
    Nficha = request.form['Nficha']
    documento = request.form['documento']
   

    new_section = registross(nombre, Apellido, Curso , Nficha,documento)
    db.session.add(new_section)
    db.session.commit()
    return "ok"



