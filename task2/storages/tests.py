import unittest

from task2.record_creator.json_record_creator import JsonRecordCreator
from task2.storages.exceptions import WrongConfigException, RecordNotFound, LimitOffsetIncompatibility
from task2.storages.local_storage import LocalStorage


class StorageTester(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        config = {
            "path": "tmp"
        }

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        filtered_records = local_storage.filter_records("json")
        for record in filtered_records:
            local_storage.delete_record(record.filename)

        config = {
            "path": "storage"
        }

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        filtered_records = local_storage.filter_records("json")
        for record in filtered_records:
            local_storage.delete_record(record.filename)

    def test_init_local_storage(self):
        config = {
            "path": "storage"
        }

        local_storage = LocalStorage(config)

        self.assertEqual(config, local_storage.config)

    def test_get_storage_local_storage(self):
        config = {
            "path": "storage"
        }

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()

        self.assertEqual("storage/", local_storage.local_path)

    def test_get_storage_local_storage_wrong_config(self):
        config = {
            "not_path": "storage"
        }

        try:
            LocalStorage(config).get_storage()
        except Exception as e:
            self.assertEqual(WrongConfigException, type(e))
            return

        self.assertTrue(False)

    def test_insert_record_local_storage(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)

        self.assertTrue(local_storage.check_record_exists(json_record.filename))

    def test_insert_records_local_storage(self):
        config = {
            "path": "storage"
        }
        name1 = "test1"
        data1 = {
            "test": True
        }
        name2 = "test2"
        data2 = {
            "test": False
        }
        records = []

        json_record_creator = JsonRecordCreator()
        json_record1 = json_record_creator.create_record(name1, data1)
        json_record2 = json_record_creator.create_record(name2, data2)
        records.append(json_record1)
        records.append(json_record2)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_records(records)

        self.assertTrue(local_storage.check_record_exists(json_record1.filename))
        self.assertTrue(local_storage.check_record_exists(json_record2.filename))

    def test_retrieve_record_local_storage(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)
        retrieved_record = local_storage.retrieve_record(json_record.filename)

        self.assertEqual(json_record.name, retrieved_record.name)
        self.assertEqual(json_record.data, retrieved_record.data)

    def test_retrieve_record_local_storage_not_found(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }
        not_found_file_name = "testt.json"

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)
        try:
            local_storage.retrieve_record(not_found_file_name)
        except Exception as e:
            self.assertEqual(RecordNotFound, type(e))
            return

        self.assertTrue(False)

    def test_update_record_local_storage(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }
        updated_name = "updated_test"
        updated_data = {
            "test": False
        }

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)
        updated_json_record = json_record_creator.create_record(updated_name, updated_data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)
        local_storage.update_record(json_record.filename, updated_json_record)
        retrieved_record = local_storage.retrieve_record(updated_json_record.filename)

        self.assertEqual(updated_json_record.name, retrieved_record.name)
        self.assertEqual(updated_json_record.data, retrieved_record.data)

    def test_update_record_local_storage_not_found(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }
        updated_name = "updated_test"
        updated_data = {
            "test": False
        }
        not_found_file_name = "testt.json"

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)
        updated_json_record = json_record_creator.create_record(updated_name, updated_data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)


        try:
            local_storage.update_record(not_found_file_name, updated_json_record)
        except Exception as e:
            self.assertEqual(RecordNotFound, type(e))
            return

        self.assertTrue(False)

    def test_delete_record_local_storage(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)
        local_storage.delete_record(json_record.filename)

        self.assertFalse(local_storage.check_record_exists(json_record.filename))

    def test_delete_record_local_storage_not_found(self):
        config = {
            "path": "storage"
        }
        name = "test"
        data = {
            "test": True
        }
        not_found_file_name = "testt.json"

        json_record_creator = JsonRecordCreator()
        json_record = json_record_creator.create_record(name, data)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_record(json_record)
        try:
            local_storage.delete_record(not_found_file_name)
        except Exception as e:
            self.assertEqual(RecordNotFound, type(e))
            return

        self.assertTrue(False)

    def test_filter_records_local_storage_no_offset_no_limit(self):
        config = {
            "path": "storage"
        }
        name1 = "test1"
        data1 = {
            "test": True
        }
        name2 = "test2"
        data2 = {
            "test": False
        }
        records = []

        json_record_creator = JsonRecordCreator()
        json_record1 = json_record_creator.create_record(name1, data1)
        json_record2 = json_record_creator.create_record(name2, data2)
        records.append(json_record1)
        records.append(json_record2)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_records(records)
        filtered_records = local_storage.filter_records("json")

        self.assertEqual(json_record1.name, filtered_records[0].name)
        self.assertEqual(json_record1.data, filtered_records[0].data)
        self.assertEqual(json_record2.name, filtered_records[1].name)
        self.assertEqual(json_record2.data, filtered_records[1].data)

    def test_filter_records_local_storage_one_offset_one_limit(self):
        config = {
            "path": "storage"
        }
        name1 = "test1"
        data1 = {
            "test": True
        }
        name2 = "test2"
        data2 = {
            "test": False
        }
        records = []

        json_record_creator = JsonRecordCreator()
        json_record1 = json_record_creator.create_record(name1, data1)
        json_record2 = json_record_creator.create_record(name2, data2)
        records.append(json_record1)
        records.append(json_record2)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_records(records)
        filtered_records = local_storage.filter_records("json", offset=1, limit=1)

        self.assertEqual(1, len(filtered_records))
        self.assertEqual(json_record2.name, filtered_records[0].name)
        self.assertEqual(json_record2.data, filtered_records[0].data)

    def test_filter_records_local_storage_offset_bigger_than_limit(self):
        config = {
            "path": "storage"
        }
        name1 = "test1"
        data1 = {
            "test": True
        }
        name2 = "test2"
        data2 = {
            "test": False
        }
        records = []

        json_record_creator = JsonRecordCreator()
        json_record1 = json_record_creator.create_record(name1, data1)
        json_record2 = json_record_creator.create_record(name2, data2)
        records.append(json_record1)
        records.append(json_record2)

        local_storage = LocalStorage(config)
        local_storage = local_storage.get_storage()
        local_storage.insert_records(records)
        try:
            local_storage.filter_records("json", offset=2, limit=1)
        except Exception as e:
            self.assertEqual(LimitOffsetIncompatibility, type(e))
            return

        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
