import json


def read_file_setting(file_path):
    file_read = open(file_path, "r")
    data = json.load(file_read)
    file_read.close()
    return data
