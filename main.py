import task2

if __name__ == "__main__":
    name = "test"
    data = {"a": 1}
    rec = task2.create_record("json", name, data)
    rec.generate_file()
    rec.delete_file()
