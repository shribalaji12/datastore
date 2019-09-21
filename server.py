"""Script to run datastore"""
import threading
import argparse
import json
import sys
from datastore import DataStore


class DataStoreOps(DataStore):
    """
    DataStore
    """
    def __init__(self, file_path=None):
        super().__init__(file_path=file_path)

    def create_data(self, data):
        if self.create(data=data):
            print(f"Data Created")
            return True

    def read_data(self, key):
        data = self.read(key=key)
        if data:
            print(data)
            return True
        return False

    def delete_data(self, key):
        data = self.delete(key=key)
        if data:
            print(data)
            return True
        return False


def run():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--file', dest='file', action='store', help='Specify file fo storage')
        parser.add_argument('-r', '--read', dest='read', action='store', help='Provide key to read from datastore')
        parser.add_argument('-c', '--create', type=json.loads, dest='post', action='store',
                            help='Provide key-value to store in datastore')
        parser.add_argument('-d', '--delete', dest='delete', action='store',
                            help='Provide key to delete from datastore')
        args = parser.parse_args()
        data = DataStoreOps(args.file)
        if args.post:
            data.create_data(args.post)
        if args.read:
            data.read_data(args.read)
        if args.delete:
            data.delete_data(args.delete)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.start()
