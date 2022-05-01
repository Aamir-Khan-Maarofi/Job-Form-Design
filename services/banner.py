from turtle import color
from termcolor import colored
from pyfiglet import Figlet

def banner():
    figlet = Figlet(font='banner3-D')
    print(colored(figlet.renderText("JOBS DB"), "green"))

if __name__ == "__main__":
    banner()