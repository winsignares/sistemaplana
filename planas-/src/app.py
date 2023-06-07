from flask import Flask, render_template
from bd import app
from bd import db





#model
from Model.validar import validar
from Model.registro import registross
from Model.plana import planass



#ruta
from rutas.home import routes_home
from rutas.validar import routes_validar
from rutas.formulario import routes_formulario 
from rutas.update import routes_mostrar 
from rutas.castigo import routes_tablacastigo 
from rutas.buscador import routes_buscador
from rutas.grafico import routes_grafico




#ubicación rutas
app.register_blueprint(routes_home, url_prefix="/fronted")
app.register_blueprint(routes_formulario , url_prefix="/fronted")
app.register_blueprint(routes_mostrar  , url_prefix="/fronted")
app.register_blueprint(routes_tablacastigo  , url_prefix="/fronted")
app.register_blueprint(routes_validar   , url_prefix="/fronted")
app.register_blueprint(routes_buscador  , url_prefix="/fronted")
app.register_blueprint(routes_grafico , url_prefix="/fronted")




@app.route("/")
def inde():
    titulo="pagina principal"
    return render_template('index.html', title=titulo)


if __name__ == '__main__':
    app.run(debug=True, port=1000, host='0.0.0.0')






 


