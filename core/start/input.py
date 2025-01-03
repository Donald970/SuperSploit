import json

try:
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    import prompt_toolkit
    from .database import jsdm, exmgt
    from .help import Help
    import os
    import sys
    from ..Logging import Logger
    import traceback
    from subprocess import Popen, PIPE, run
    from .use import Use
    from .. import exploit
except ImportError as e:
    from .database import jsdm, exmgt
    from .help import Help
    import os
    import sys
    from ..Logging import Logger
    import traceback
    from subprocess import Popen, PIPE
    from .use import Use
    from .exploit import exploit
    Logger.__start_logger_object__(str(e))
    pass

config = f"/home/{os.getlogin()}/SuperSploit/.data/.config/config.json"
from ..Logging import Logger
with open(config, 'r') as file:
    config_dict = json.load(file)
    file.close()

install_location = config_dict["install_location"]
data_install_location = config_dict["data install location"]
database = config_dict["database location"]
his = FileHistory(f"{data_install_location}/.history")
prompt = prompt_toolkit.PromptSession(history=his, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)


class Input(Logger):

    def __init__(self):
        self.inputs = ["show", "update", "set", "add", "del", "help", "search", "use", "exploit"]
        self.functions = [jsdm.show_db_triger, exmgt.updateDb, jsdm.set, jsdm.add, jsdm.Del, Help.help, exmgt.search, Use.use, exploit.exploit]
        self.encoded_data = b""
        self.get()
        self.handle_data()
        return

    @classmethod
    def config_check(cls):
        cls.shell = config_dict["shell"]
        return

    def get(self) -> None:
        try:
            data = prompt.prompt("[SuperSploit]: ")
            self.encoded_data = data.encode()
            return
        except ImportError:
            data = input("[SuperSploit]: ")
            self.encoded_data = data.encode()
            return

    def handle_data(self):
        dataStr = self.encoded_data.decode()
        if "exit" in dataStr:
            sys.exit()
        try:
            self.functions[self.inputs.index(dataStr.split(" ")[0])](dataStr)
            return True
        except Exception:
            a = traceback.format_exc()
            if "ValueError" not in a:
                self.__start_logger_object__(a)
            if "ValueError" in a:
                if self.shell:
                    try:
                        proc = run(dataStr.split(' '), capture_output=True)
                        if len(proc.stderr) != 0:
                            print(proc.stderr.decode())
                        else:
                            print(proc.stdout.decode())
                        return
                    except FileNotFoundError as e:
                        self.__start_logger_object__(str(traceback.format_exc()))
                        print(f"{dataStr} not found on system")
                else:
                    print(f"to run as a command change the shell value in {config} file to true")
        return True