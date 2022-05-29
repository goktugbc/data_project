# Task 1
- Stack has been implemented
- Unit tests have been implemented

# Task 2
- Store and retrieve data library has been implemented for data type json and storage type local storage
  - create_record function gets format(json), name and data
  - get_storage function gets config to create/get storage. In our case, it gets a config that has local path
  - insert_record function gets storage and record to be inserted
  - insert_records function gets storage and records list to be inserted
  - retrieve_record function gets storage and file name to be retrieved
  - filter_records function gets storage, record format(to query format), limit and offset values
  - update_record function gets storage, file name(file name of the record to be updated) and record(record object that will be updated version)
  - delete_record function gets storage, file name(file name of the record to be deleted)
- Unit tests of inner modules of the library have been implemented
- Mock storage and record format modules have been created and have not been implemented