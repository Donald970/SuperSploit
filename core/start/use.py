import os
import json
from core.start.database import jsdm


config = f"/home/{os.getlogin()}/SuperSploit/.data/.config/config.json"
from ..Logging import Logger
with open(config, 'r') as file:
    config_dict = json.load(file)
    file.close()

install_location = config_dict["install_location"]
data_install_location = config_dict["data install location"]
database = config_dict["database location"]


class Use:
    def __init__(self):
        return 
    
    @classmethod
    def exploits(cls, data):
        exploits = []
        for x in os.listdir(f"{install_location}/exploits"):
            for i in os.listdir(f"{install_location}/exploits/{x}"):
                file = f"{install_location}/exploits/{x}/{i}"
                exploits.append(file)
        db = jsdm.checkDb()
        db["EXPLOIT"] = exploits[int(data.split(" ")[2])]
        jsdm.update(db)
        return
    
    @classmethod
    def payloads(cls, data):
        payloads = []
        for x in os.listdir(f"{install_location}/payloads"):
            for i in os.listdir(f"{install_location}/payloads/{x}"):
                file = f"{install_location}/payloads/{x}/{i}"
                payloads.append(file)
        db = jsdm.checkDb()
        db["PAYLOAD"] = payloads[int(data.split(" ")[2])]
        jsdm.update(db)
        return
    
    @classmethod
    def use(cls, data):
        data1 = data.split(" ")[1]
        data_list = ["exploit", "payload"]
        funcs = [cls.exploits, cls.payloads]
        for i in data_list:
            if data1 == i:
                funcs[data_list.index(data1)](data)
        return
