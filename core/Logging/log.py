from os import getlogin
install_location = f"/home/{getlogin()}/SuperSploit"
data_location = f"{install_location}/.data/.dev_logs"
import traceback
class Logger:
    def __init(self):
        return

    @classmethod
    def __start_logger_object__(cls, data: str):
        with open(f"{data_location}", "a") as file:
            data = data =+ "\n"
            file.write(data)
            file.close()
            return


