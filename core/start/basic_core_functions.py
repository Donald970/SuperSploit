#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
import sys, subprocess
from .database import jsdm, exmgt
from .use import Use
from .exploit import exploit
install_location = f"/home/{os.getlogin()}/SuperSploit"
data_install_location = f"/home/{os.getlogin()}/SuperSploit/.data"
database = f"{install_location}/.data"


class bcf:

    def __init__(self):
        return

    @staticmethod
    def updateDb(da):
        try:
            sys.stdout.write("Updating exploit details database. \n")
            vars = []
            oldDb = jsdm.checkDb()
            for x in os.listdir(f"{install_location}/exploits"):
                for i in os.listdir(f"{install_location}/exploits/{x}"):
                    file = f"{install_location}/exploits/{x}/{i}"
                    with open(file, "r") as rfile:
                        data = rfile.read().split("# DETAILS #")
                        rfile.close()
                        fileList = str(data[1]).split("\n")
                        for z in fileList:
                            if fileList.index(z) > 0:
                                if fileList.index(z) == len(fileList) -1:
                                    break
                                vars.append(z)
            for s in vars:
                k = s.split(" ")[1]
                if k not in oldDb:
                    oldDb[k] = None
            jsdm.update(oldDb)
        except Exception as e:
            print(e)

    @classmethod
    def help(cls, data):
        if len(data) > len("help"):
            sys.stdout.write("not implemented yet \n")
            return
        with open(f"{install_location}/.data/.help/help") as file:
            sys.stdout.write(f"{file.read()} \n")
            file.close()
            return

    @classmethod
    def handle_data(cls, data):
        if data == "exit":
            sys.exit()
        inputs = ["show", "update", "set", "add", "del", "help", "search", "use", "exploit"]
        funcs = [jsdm.showBD, cls.updateDb, jsdm.set, jsdm.add, jsdm.Del, cls.help, exmgt.search, Use.use, exploit.exploit]
        if data.split(" ")[0] not in inputs:
            try:
                subprocess.run(data.split(' '))
                return
            except Exception as e:
                if "[Errno 13]" in str(e):
                    return
                sys.stdout.write(str(e))
        try:
            funcs[inputs.index(data.split(" ")[0])](data)
            return True
        except Exception as e:
            sys.stdout.write(f"{str(e)}\n")
            return

    @staticmethod
    def getData():
        try:
            import prompt_toolkit
            from prompt_toolkit.history import FileHistory
            from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
        except ImportError:
            pass
        try:
            his = FileHistory(f"{data_install_location}/.history")
            inputa = prompt_toolkit.PromptSession(history=his, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
            return inputa.prompt("superploit: ")
        except NameError:
            return input("superploit: ")
