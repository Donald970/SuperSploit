import os, json
shell_prompt = 'Set shell value in config to true [y/n]:'
install_location = f"/home/{os.getlogin()}/SuperSploit"
data_install_location = f"{install_location}/.data"
database = f"{install_location}/.data/data.json"
config = f"{data_install_location}/.config/config.json"
shell = True if input(shell_prompt).startswith("y") else False
path = os.getenv("PATH")
config_dict = {"shell": shell,
               "install_location": install_location,
               "database location": database,
               "data install location": data_install_location,
               "PATH": path
               }


"""{



Lets use this space to create a alias database





}"""


print("writing config file")
with open(config, "w") as file:
    file.write(json.dumps(config_dict, sort_keys=True, indent=4))
    file.close()
print("Setup finished.")