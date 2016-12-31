#mongodb://<dbuser>:<dbpassword>@ds027425.mlab.com:27425/techfood
import mongoengine
import json
#mongodb://<dbuser>:<dbpassword>@ds043022.mlab.com:43022/my_note
host = "ds043022.mlab.com"
port = 43022
db_name = "my_note"
user_name = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    return json.loads(item.to_json())