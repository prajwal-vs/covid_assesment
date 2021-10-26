from flask import request
from flask_restful import Resource, reqparse
import json
from commons.json_utils import to_json
from services.user_service import userService


class Users(Resource):
    def __init__(self):
        self.service = userService()

    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        response = self.service.addUser(data)
        return response


class selfAssesment(Resource):
    def __init__(self):
        self.service = userService()

    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        response = self.service.addSelfAssesment(data)
        return response



