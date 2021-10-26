import os
import json
import datetime


class Helpers:
    def readJsonData(self, file_name):
        with open(os.path.join('database', file_name), 'r') as database:
            return json.loads(database.read())

    def writeJsonData(self, file_name, data):
        with open(os.path.join('database', file_name), 'w+') as database:
            database.write(json.dumps(data))
