from utils.json_util import read_json

def get_login_data(filepath,logintype):
    data =[]
    for item in read_json(filepath):
        if item["login_type"]==logintype:
            data.append(item)
    return data




