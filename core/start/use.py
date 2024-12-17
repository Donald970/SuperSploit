import os
import sys
import json

from .database import jsdm

install_location = f"/home/{os.getlogin()}/SuperSploit"
data_install_location = f"/home/{os.getlogin()}/SuperSploit/.data"
database = f"{install_location}/.data"

class Use:
    def __init__(self):
        return 
    
    @classmethod
    def use(cls, da):
        exploits = []
        for x in os.listdir(f"{install_location}/exploits"):
            for i in os.listdir(f"{install_location}/exploits/{x}"):
                file = f"{install_location}/exploits/{x}/{i}"
                exploits.append(file)
        db = jsdm.checkDb()
        db["EXPLOIT"] = exploits[int(da.split(" ")[2])]
        jsdm.update(db)
        return
