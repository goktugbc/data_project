import unittest

from task2.record_creator.record.exceptions import WrongFormatException
from task2.record_creator.record.json_record import JsonRecord


class RecordTester(unittest.TestCase):
    def test_init_json_record(self):
        name = "test"
        data = {
            "test": True
        }

        json_record = JsonRecord(name, data)

        self.assertEqual(name, json_record.name)
        self.assertEqual(data, json_record.data)

    def test_generate_file_json_record(self):
        name = "test"
        data = {
            "test": True
        }
        tmp_path = "tmp/"

        json_record = JsonRecord(name, data)
        file_path = json_record.generate_file()

        self.assertEqual(tmp_path + json_record.filename, file_path)

        from os.path import exists

        self.assertTrue(exists(file_path))

    def test_delete_file_json_record(self):
        name = "test"
        data = {
            "test": True
        }

        json_record = JsonRecord(name, data)
        file_path = json_record.generate_file()

        json_record.generate_file()
        json_record.delete_file()

        from os.path import exists

        self.assertFalse(exists(file_path))

    def test_dump_data_and_load_data_json_record(self):
        name = "test"
        data = {
            "test": True
        }

        json_record = JsonRecord(name, data)

        dumped_data = json_record.dump_data()

        self.assertTrue(isinstance(dumped_data, str))

        json_record.data = dumped_data
        loaded_data = json_record.load_data()

        self.assertTrue(isinstance(loaded_data, dict))


if __name__ == '__main__':
    unittest.main()
