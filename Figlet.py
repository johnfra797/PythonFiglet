import pyfiglet
class Figlet:
    def __init__(self, str):
        result=pyfiglet.figlet_format(str)
        print(result)

