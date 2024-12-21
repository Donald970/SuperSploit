# This is the class responsible for all the json database managment
#  database.py
#  
#  Copyright 2024 donaldford05091997 <donaldford05091997@penguin>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import sys
import json
from ..Logging import Logger
install_location = f"/home/{os.getlogin()}/SuperSploit"
data_install_location = f"{install_location}/.data"
database = f"{install_location}/.data"


class jsdm(Logger):
    def __init__(self):
        return
	
    @classmethod
    def checkDb(cls):
        try:
            if os.path.exists(install_location):
                if os.path.exists(database):
                    with open(f"{database}/data.json") as file:
                        data = json.load(file)
                        file.close()
                        return data
                else:
                    sys.stderr.write("[!] Database file not found!")
                    os.mkdir(database)
                    with open(f"{database}/data.json", "w") as file:
                        data = {"HOST ": "", "PORT": 0}
                        file.write(json.dumps(data))
                        file.close()
                    return data
            else:
                os.mkdir(install_location)
                with open(f"{database}/data.json", "w") as file:
                    data = {"HOST ": "", "PORT": 0}
                    file.write(json.dumps(data))
                    file.close()
                return data
        except Exception as e:
            cls.__start_logger_object__(str(e))
            print(e)

    @staticmethod
    def update(data):
        with open(f"{database}/data.json", "w") as file:
            file.write(json.dumps(data, sort_keys=True, indent=4))
            file.close()
        return data

    @classmethod
    def showBD(cls, da):
        try:
            for k, v in cls.checkDb().items():
                sys.stdout.write(f"{k} = {v}\n")
            return
        except Exception as e:
             print(e)

    @classmethod
    def set(cls, data):
        oldDB = cls.checkDb()
        dataL = data.split(" ")
        if len(dataL) < 3:
            sys.stderr.write("Improper format")
        x = dataL[1]
        y = dataL[2]
        for k, v in oldDB.items():
            if x == k:
                oldDB[k] = y
        cls.update(oldDB)
        return True

    @classmethod
    def add(cls, data):
        db = cls.checkDb()
        datal = data.split(" ")
        if len(datal) < 3:
            print("Improper format.")
            return
        db[datal[1]] = datal[2]
        cls.update(db)
        return

    @classmethod
    def Del(cls, data):
        db = cls.checkDb()
        datal = data.split(" ")
        if len(datal) < 2:
            sys.stderr.write("Improper format.")
            return
        db1 = {}
        for k, v in db.items():
            if datal[1] in k:
                pass
            else:
                db1[k] = v
        cls.update(db1)
        return

class exmgt(jsdm):
    
    @classmethod
    def search(cls, da):
        try:
            if da.split(" ")[1] == "exploits":
                """add the ability to search outside install locations"""
                exploits = []
                for x in os.listdir(f"{install_location}/exploits"):
                    for i in os.listdir(f"{install_location}/exploits/{x}"):
                        file = f"{install_location}/exploits/{x}/{i}"
                        exploits.append(file)

                daL = da.split(" ")
                searches = daL[2:]
                if len(searches) == 0:
                    for i in exploits:
                        print(f"{exploits.index(i)}: {i}")
                    return
                for x in searches:
                    print(f"search results for {x}")
                    for y in exploits:
                        if x in y:
                            print(f"{exploits.index(y)}: {y}")
                return

            if da.split(" ")[1] == "payloads":
                """add the ability to search outside install locations"""
                payloads = []
                for x in os.listdir(f"{install_location}/payloads"):
                    for i in os.listdir(f"{install_location}/payloads/{x}"):
                        file = f"{install_location}/payloads/{x}/{i}"
                        payloads.append(file)

                daL = da.split(" ")
                searches = daL[2:]
                if len(searches) == 0:
                    for i in payloads:
                        print(f"{payloads.index(i)}: {i}")
                    return
                for x in searches:
                    print(f"search results for {x}")
                    for y in payloads:
                        if x in y:
                            print(f"{payloads.index(y)}: {y}")
                return
        except Exception as e:
            return e

    @staticmethod
    def get_all_exploits():
        exploits = []
        for x in os.listdir(f"{install_location}/exploits"):
            for i in os.listdir(f"{install_location}/exploits/{x}"):
                file = f"{install_location}/exploits/{x}/{i}"
                exploits.append(file)
        return exploits
