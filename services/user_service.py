from commons.helper import Helpers
from uuid import uuid4

from commons.json_utils import to_json


class userService:
    def __init__(self):
        self.helper = Helpers()

    def addUser(self, data):
        try:
            users = self.helper.readJsonData('users.json')
            for user in users:
                if users[user]['phoneNumber'] == data['phoneNumber']:
                    return to_json('user exist', is_error=True)
            data['user_id'] = str(uuid4())
            users.update({data['user_id']: data})
            self.helper.writeJsonData('users.json', users)
            return {'user_id': data['user_id']}

        except Exception as e:
            return to_json(e, is_error=True)

    def addSelfAssesment(self, data):
        try:
            riskPercentage = 0
            if not data['travelHistory'] and not data['symptoms'] and not data['contactWithCovidPatient']:
                riskPercentage = 5
            elif data['travelHistory'] or data['contactWithCovidPatient']:
                if len(data['symptoms']) == 1:
                    riskPercentage = 50
                elif len(data['symptoms']) == 2:
                    riskPercentage = 75
                elif len(data['symptoms']) > 2:
                    riskPercentage = 95
            users = self.helper.readJsonData('users.json')
            for user in users:
                if user == data['user_id']:
                    data['riskPercentage'] = riskPercentage
                    users[user]['symptoms'] = data
                    self.helper.writeJsonData('users.json', users)
                    return {'riskPercentage': data['riskPercentage']}
            return to_json("Users doesn't exist", is_error=True)

        except Exception as e:
            return to_json(e, is_error=True)
