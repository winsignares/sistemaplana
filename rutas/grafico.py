from bd import db
from flask import Blueprint, jsonify 
from Model.registro import registross
from Model.plana import planass
from sqlalchemy import func



routes_grafico = Blueprint("routes_grafico ", __name__)


@routes_grafico.route('/graficos', methods=['GET'])
def mostarcastigo():
    resultado = db.session.query(registross.nombre.label('nombre_persona'), func.sum(planass.Planas).label('total_planas')).select_from(registross).join(planass).group_by(registross.nombre).all()  
    data = [{'nombre_persona': row.nombre_persona, 'total_planas': row.total_planas} for row in resultado]
    return jsonify(data)
    

    
