"""DataStore library"""

import os
import json
import datetime


class DataStore:

    def __init__(self, file_path=None):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        self.file = os.path.join(file_path, 'data.json') if file_path else "data.json"
        self.file_obj = None
        self.data = None

    def read_datastore(self):
        # create file if does not exist
        if not os.path.exists(self.file):
            file_data = []
            with open(self.file, 'w+') as obj:
                obj.write(str(file_data))
            return False
        # read data from file
        with open(self.file, 'r+') as file_obj:
            self.file_obj = file_obj
            try:
                self.data = json.load(file_obj)
                return True
            except json.decoder.JSONDecodeError:
                self.data = []

    def create(self, data):
        data['created_at'] = datetime.datetime.now().isoformat()
        if data.get('expiry'):
            expiry_at = datetime.datetime.now() + datetime.timedelta(seconds=data.get('expiry'))
            data['expiry_at'] = expiry_at.isoformat()
        if not self.read_datastore():
            with open(self.file, 'w+') as file_obj:
                self.file_obj = file_obj
                json.dump([data], self.file_obj, indent=4)
            return True
        with open(self.file, 'w+') as file_obj:
            self.file_obj = file_obj
            try:
                json.dump(sum([self.data, [data]], []), self.file_obj, indent=4)
                return True
            except json.decoder.JSONDecodeError:
                pass

    def read(self, key):
        if not self.read_datastore():
            return f"No data found"
        res_data = None
        for data in self.data:
            if list(data.keys())[0] == key:
                res_data = data
                break
        if res_data:
            if res_data.get('expiry') and datetime.datetime.now() > \
                    datetime.datetime.strptime(res_data.get('expiry_at'), '%Y-%m-%dT%H:%M:%S.%f'):
                return f"Key expired"
        return res_data if res_data else f"No data found"

    def delete(self, key):
        if not self.read_datastore():
            return f"No data found"
        print(self.data)
        print(key)
        key_data = list(filter(lambda x: list(x.keys())[0] == key, self.data))[0]
        if key_data.get('expiry')\
                and datetime.datetime.now() > datetime.datetime.strptime(
                key_data.get('expiry_at'), '%Y-%m-%dT%H:%M:%S.%f'):
            return f"Key expired"
        new_data = filter(lambda x: list(x.keys())[0] != key, self.data)
        if new_data:
            with open(self.file, 'w+') as file_obj:
                json.dump(eval(json.dumps(list(new_data))), file_obj, indent=4)
            return True
        return f"Key not found"
