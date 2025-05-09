from flask_restful import Resource, Api, abort
from flask import request
from . import bp_api
from .models import Fail_Machine
from .schemas import FailSchema

api = Api(bp_api)

class FailApiResource(Resource):
    def get(self):
        
        data = Fail_Machine.get_all()
        fail_schema = FailSchema(many=True)

        context = {
            'status':True,
            'message':'Historial de estados',
            'content':fail_schema.dump(data)
        }

        return context, 200
    
    def post(self):
        data = request.get_json()
        codigo = data.get('codigo')
        aq = data.get('aq')
        uss = data.get('uss')
        voc = data.get('voc')
        temperature = data.get('temperature')
        fail = Fail_Machine(codigo, aq, uss, voc, temperature)
        fail.save()

        data_schema = FailSchema()

        context = {
            'status':True,
            'message':'Estado registrado',
            'content':data_schema.dump(fail)
        }
        return context, 201

class FailApiResourceDetail(Resource):

    def get_estado(self,id):

        registro = Fail_Machine.get_by_id(id)
        if not registro:
            abort(404, message="Estado no registrado")
        
        return registro
    
    def get(self, id):
        data = self.get_estado(id)
        data_schema = FailSchema()

        context = {
            'status':True,
            'message':'Estado encontrado',
            'content':data_schema.dump(data)
        }

        return context
    
    def put(self, id):
        data = request.get_json()

        estado = self.get_estado(id)
        estado.codigo = data.get('codigo')
        estado.aq = data.get('aq')
        estado.uss = data.get('uss')
        estado.voc = data.get('voc')
        estado.temperature = data.get('temperature')
        estado.save()

        data_schema = FailSchema()

        context = {
            'status':True,
            'message':'Estado actualizado',
            'content':data_schema.dump(estado)
        }

        return context
    
    def delete(self, id):
        estado = self.get_estado(id)
        estado.delete()

        context = {
            'status':True,
            'message':'Estado eliminado'
        }

        return context, 204

api.add_resource(FailApiResource, '/')
api.add_resource(FailApiResourceDetail, '/<int:id>')