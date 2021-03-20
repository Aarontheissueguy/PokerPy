import pickle
import os
class Helpers:

    def open_file(self, filename, mode="r+"):
        try:
            f = open(filename, mode)
        except:
            file_path = "{}/{}".format(storage_dir, filename)
            f = open(file_path, mode)

        return f

    def read_file(self, filename):
        filepath = filename
        if os.path.exists(filepath):
            file = self.open_file(filepath, "rb")
            return pickle.load(file)


    def save_data(self, filepath, value):
        save_file = self.open_file(filepath, "wb")
        pickle.dump(value, save_file)
        print("saved")

helpers = Helpers()
