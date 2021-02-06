import json


def write_file_setting(file_path, new_data):
    file_write = open(file_path, "w")
    json.dump(new_data, file_write)
    file_write.close()
