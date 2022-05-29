from task2.storages import Storage
from task2.storages.exceptions import WrongConfigException


class LocalStorage(Storage):
    local_path = ""

    def __init__(self, config):
        super().__init__(config)

    def get_storage(self):
        if "path" not in self.config:
            raise WrongConfigException

        import os

        self.local_path = self.config["path"]
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        return self