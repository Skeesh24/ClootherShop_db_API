from os import environ


def toDesktop(any):
    with open(f'C:/Users/{environ.get("USERNAME")}/Desktop/out.txt', 'w') as file:
        file.write(repr(any).replace("'", ""))
