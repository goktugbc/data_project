from abc import ABC, abstractmethod


class Record(ABC):
    name = ""
    data = None

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def generate_file(self):
        import os

        tmp_path = "tmp/"

        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)

        f = open(tmp_path + self.filename, "w")
        f.write(self.dump_data())
        f.close()

        return tmp_path + self.filename

    def delete_file(self):
        import os
        filename = self.name + ".json"
        os.remove("tmp/" + filename)

    @abstractmethod
    def dump_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass
