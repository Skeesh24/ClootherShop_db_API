import os


LOG_PATH = os.curdir+"/logs"


def log(smth):
    os.mkdir(LOG_PATH)
    with open(f"C:/Users/{os.environ.get('USERNAME')}/Desktop/out.txt", "w") as file:
        file.write(str(smth).replace("\'", '\"').lower())
