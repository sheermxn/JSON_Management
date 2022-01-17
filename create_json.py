from os.path import dirname, realpath, isfile
from json import dump


class JsonManager():

    def __init__(self):
        self.dir = dirname(realpath(__file__)) + '/'
    def CreateJSON(self, file):
        data = {"username": "", "password": ""}
        path_data_json = self.dir + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                dump(data, f, indent=2, separators=(',', ': '))
            return True
        else:
            return False

if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.CreateJSON('data/data.json')