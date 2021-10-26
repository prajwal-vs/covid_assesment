#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Flask base application declaration and URL configuration."""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.admin import Admin, covidResult

from resources.users import Users, selfAssesment

app = Flask(__name__)
CORS(app)
api = Api(app)

# http://server/api/v1/test
# api.add_resource(healthCheck, '/api/v1/test')

api.add_resource(Users, '/api/v1/users')

api.add_resource(Admin, '/api/v1/admin')

api.add_resource(covidResult, '/api/v1/admin/updateCovidResult')

api.add_resource(selfAssesment, '/api/v1/user/selfAssessment')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
