import json
import os

config = f"/home/{os.getlogin()}/SuperSploit/.data/.config/config.json"
with open(config, 'r') as file:
    config_dict = json.load(file)
    file.close()

install_location = config_dict["install_location"]
data_install_location = config_dict["data install location"]
database = config_dict["database location"]

class Help:
    def __init__(self):
        return

    @classmethod
    def help(cls, data):
        print(data)
        if len(data.split(" ")) > 1:
            if '' in data.split(' '):
                with open(f"{data_install_location}/.help/help") as file:
                    print(f"{file.read()}")
                    file.close()
                return
            else:
                with open(f"{data_install_location}/.help/{data.split(' ')[1]}") as file:
                    print(f"{file.read()}")
                    file.close()
            pass
        else:
            with open(f"{data_install_location}/.help/help") as file:
                print(f"{file.read()} \n")
                file.close()
                return