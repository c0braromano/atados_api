from flask_restful import Resource
from flask import request
from funcoes.selecionar_lucro import selecionar_lucro


class retornarLucro(Resource):
    def post(self):
        dados = request.get_json()

        return selecionar_lucro(dados['precos'])