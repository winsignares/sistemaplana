
from bd import db
from flask import Blueprint, request, session , redirect ,  render_template , jsonify
from Model.validar import validar
from random import randint
import smtplib
import email
from datetime import datetime, timezone
import secrets
import hashlib
from flask import sessions
import random
from datetime import datetime , timedelta




routes_olvidado = Blueprint("routes_olvidados", __name__)



@routes_olvidado.route('/verificarcorreo', methods=["POST"])
def correo():
    correos = request.json["gmails"]
    verificacions = db.session.query(validar).filter(validar.correo == correos).first()
    print(verificacions)

    if verificacions:
        session['gmails'] = verificacions.correo
        return "a"
    else:
        return "Correo no válido"





@routes_olvidado.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    fullcorreo = request.json['fullcorreo']

    # Check if the user has exceeded the request limit
    now = datetime.now(timezone.utc)  # Convert to offset-aware datetime in UTC
    elapsed_time = timedelta(minutes=5)  # Valor predeterminado de 5 minutos
    request_count = 0


    if 'last_request_time' in session and 'request_count' in session:
        last_request_time = session['last_request_time']
        request_count = session['request_count']
        elapsed_time = now - last_request_time

        # Calculate the time remaining until the limit resets
        time_to_wait = timedelta(minutes=5 + (request_count - 1)) - elapsed_time
        hours = time_to_wait.seconds // 3600
        minutes = (time_to_wait.seconds % 3600) // 60
        seconds = time_to_wait.seconds % 60

        if elapsed_time < timedelta(minutes=5 + (request_count - 1)) and request_count >= 5:
            return jsonify({'message': f'Too many requests. Please try again in {hours} hour(s), {minutes} minute(s), and {seconds} second(s).', 'time_to_wait': time_to_wait.total_seconds()}), 429

    # Check if the user exists in the database
    user = validar.query.filter_by(correo=fullcorreo).first()
    print(fullcorreo)
    if user:
        # Generate a verification code based on the user's email hash
        code_list = random.sample(range(10), 4)
        code = ''.join(str(digit) for digit in code_list)

        # Save the code in the session
        session['verification_code'] = code

        # Send an email to the user with the code
        sender_email = 'denteloofficial@gmail.com'
        sender_password = 'nyppfccmwhalhdyx'
        receiver_email = fullcorreo
        message = f'Subject: Verification Code\n\nYour verification code is: {code}'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        # Reset the request count if the time has elapsed
        if elapsed_time >= timedelta(minutes=5 + (request_count - 1)):
            session['request_count'] = 1
        else:
            # Update the session with the request count and the last request time
            session['request_count'] = session.get('request_count', 0) + 1
        session['last_request_time'] = now

        return jsonify({'message': 'Verification code sent.'})
    else:
        return jsonify({'message': 'Email not found.'}), 404







# @routes_olvidado.route('/verificarcode', methods=['POST'])
# def verificarcode():
#     verification_code = request.json['verification_code']
#     stored_code = session.get('verification_code')
    
#     if verification_code == stored_code:
#         # Si el código es correcto, redireccionar al usuario a la página de cambio de contraseña
#         response_body = {'message': 'Código verificado correctamente'}
#         status = 200
#         session.pop('verification_code', None)
#         return jsonify(response_body), status
#     else:
#         # Si el código no es correcto, devolver un error
#         response_body = {'message': 'El código ingresado es incorrecto. Inténtalo de nuevo.'}
#         status = 401
#         return jsonify(response_body), status
    

    

# @routes_olvidado.route('/actualizar_contrasena', methods=['POST'])
# def actualizar_contrasena():
#     correo = request.form['email']
#     nueva_contrasena = request.form['nueva_contrasena']

#     usuario = validar.query.filter_by(CorreoElectronico=correo).first()

#     if usuario:
#         usuario.Contrasena = nueva_contrasena
#         db.session.commit()
#         return "Contraseña actualizada correctamente"
#     else:
#         return "Usuario no encontrado"
    
# @routes_olvidado.route('/obtener_datos', methods=['POST'])
# def obtener_datos():
#     fullemail = request.json['fullemail']
#     users = validar.query.filter_by(correo=fullemail).first()
    
#     if users:
#         datos = dump(validar)
#         return jsonify(datos)
    
#     return jsonify({'mensaje': 'Correo electrónico no encontrado'}), 404


