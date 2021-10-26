from flask import request
from flask_restful import Resource, reqparse
import json
from commons.json_utils import to_json
from services.admin_service import adminService


class Admin(Resource):
    def __init__(self):
        self.service = adminService()

    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        response = self.service.addAdmin(data)
        return response


class covidResult(Resource):
    def __init__(self):
        self.service = adminService()

    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        response = self.service.updateCovidResult(data)
        return response
