import json
import os


class read_inform():
    def __init__(self):
        self.seu = self.api = self.gps_inform = {}
        self.serverchan = "0"
        self.load_json()

    def load_json(self):
        f = open('env.json','r')
        inform = json.load(f)
        self.seu = inform["seu_account"]
        self.api = inform["baidu_map_account"]
        self.gps_inform = inform["gps_inform"]
        self.serverchan = inform['serverchan']
        f.close()
