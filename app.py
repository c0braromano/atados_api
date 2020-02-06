from flask import Flask
from flask_restful import Api

from resources.metodos import retornarLucro

app = Flask(__name__)
api = Api(app)

api.add_resource(retornarLucro, '/lucro')

if __name__ == '__main__':
    app.run(debug=True)
