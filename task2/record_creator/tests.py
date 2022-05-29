import unittest

from task2.record_creator.json_record_creator import JsonRecordCreator
from task2.record_creator.record.json_record import JsonRecord


class RecordCreatorTester(unittest.TestCase):
    def test_init_json_record(self):
        name = "test"
        data = {
            "test": True
        }

        json_record_creator = JsonRecordCreator()

        self.assertTrue(isinstance(json_record_creator, JsonRecordCreator))

    def test_json_record_creator_create_record(self):
        name = "test"
        data = {
            "test": True
        }

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        self.assertTrue(isinstance(json_record_creator, JsonRecordCreator))
        self.assertTrue(isinstance(json_record, JsonRecord))
        self.assertEqual(name, json_record.name)
        self.assertEqual(data, json_record.data)


if __name__ == '__main__':
    unittest.main()
