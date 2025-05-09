from utils.db import db
from fail_predictor import FailPredictor

class Fail_Machine(db.Model):
    __tablename__ = 'fail_machine'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(6), nullable=False)
    aq = db.Column(db.Integer, nullable=False)
    uss = db.Column(db.Integer, nullable=False)
    voc = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    fail = db.Column(db.Float, nullable=True)

    def __init__(self, codigo, aq, uss, voc, temperature):
        self.codigo = codigo
        self.aq = aq
        self.uss = uss
        self.voc = voc
        self.temperature = temperature
        self.fail = 0
    
    @staticmethod
    def get_all():
        return Fail_Machine.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Fail_Machine.query.get(id)
    
    def save(self):
        ml_fail = FailPredictor()
        self.fail = ml_fail.predict(self.aq, self.uss, self.voc, self.temperature)

        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
