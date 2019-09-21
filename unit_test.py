import unittest
from server import DataStoreOps


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        file_path = 'test/'
        cls.data_store = DataStoreOps(file_path)

    def test_create(self):
        return self.data_store.create_data({"key": {"value": "hello"}, "expiry": 30})

    def test_read(self):
        assert self.data_store.read_data(key='key')

    def test_delete(self):
        assert self.data_store.delete_data(key='key')


if __name__ == '__main__':
    unittest.main()
