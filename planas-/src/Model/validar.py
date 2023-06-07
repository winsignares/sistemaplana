from bd import db, app, ma  

class validar(db.Model):
    __tablename__ = "validar"
    
    id = db.Column(db.Integer, primary_key=True)
    Ndocumento  = db.Column(db.Integer)
    contraseña = db.Column(db.String(111))
    
     
    def __init__(self, Ndocumento, contraseña):
        self.Ndocumento = Ndocumento
        self.contraseña = contraseña        

with app.app_context():
    db.create_all()

class validarSchema(ma.Schema):
    class Meta:
        fields = ('id','Ndocumento', 'contraseña')