from flask import Flask
from flask_restful import Resource, Api, reqparse
from Splitter import Splitter

app = Flask(__name__)
api = Api(app)


class ApiHandler(Resource):
    @staticmethod
    def get():
        data = {
            'success': False,
            'message': '',
            'data': {}
        }
        parser = reqparse.RequestParser()
        try:
            parser.add_argument('input', required=True)
        except:
            data['success'] = False
            data['message'] = 'No argument passed'
            return data, 400
        args = parser.parse_args()

        try:
            splitter = Splitter(args['input']).start_split()
            data['success'] = True
            data['message'] = 'Success'
            data['data'].update(splitter)
            return data, 200
        except:
            data['success'] = False
            data['message'] = 'Invalid Url'
            return data, 400

    pass


api.add_resource(ApiHandler, "/A.I.S.H.A/intentFromInput")
