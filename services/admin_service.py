from commons.helper import Helpers
from uuid import uuid4

from commons.json_utils import to_json


class adminService:
    def __init__(self):
        self.helper = Helpers()

    def addAdmin(self, data):
        try:
            users = self.helper.readJsonData('admin.json')
            for user in users:
                if users[user]['phoneNumber'] == data['phoneNumber']:
                    return to_json('Admin user already exist', is_error=True)
            data['admin_id'] = str(uuid4())
            users.update({data['admin_id']: data})
            self.helper.writeJsonData('admin.json', users)
            return {'admin_id': data['admin_id']}

        except Exception as e:
            return to_json(e, is_error=True)

    def updateCovidResult(self, data):
        try:
            admin_users = self.helper.readJsonData('admin.json')
            users = self.helper.readJsonData('users.json')
            if data['user_id'] not in users or data['admin_id'] not in admin_users:
                return to_json("user and or admin doesn't exist", is_error=True)
            pincode = users[data['user_id']]['pinCode']
            zonal_data = self.helper.readJsonData('admin.json')
            if pincode in zonal_data:
                zonal_data[pincode].append(data)
                self.helper.writeJsonData('zonal_data.json', zonal_data)
            else:
                result = dict()
                result[pincode] = []
                result[pincode].append(data)
                self.helper.writeJsonData('zonal_data.json', result)
            return {"updated": True}

        except Exception as e:
            return to_json(e, is_error=True)
