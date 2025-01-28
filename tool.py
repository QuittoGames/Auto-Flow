import os
import platform
from dataclasses import dataclass
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from data import data
from command import comamnds
import speech_recognition as sr
from googlesearch import search
from time import sleep
import threading

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def set_window():
        try:
            StartUI = QWidget()
            StartUI.resize(data.resolutionX,data.resolutionY)
            Title = QLabel("Auto Flow")
            StartUI.setWindowTitle("Auto Flow")
            Setings = QPushButton()
            StartUI.show()
        except Exception as E:
            print(f"Erro Al Inicar Interface, Erro: {E}")
    
    def google(promt):
        for url in search(promt, num_results=5):
            print(url)
        return
    
    def start_command(promt):
        promt = str(promt)
        if promt.lower().strip() not in comamnds.commands_List:
            tool.google(promt=promt)  
            sleep(3)
            return
    
        
        for i in comamnds.commands:
            if i["user_command"] in promt.lower().strip():
                print(f"Launching {i['event']}...")
                if ".exe" in i["event"]:
                    os.system("start"+ " " + i["event"])
                elif "https" in i["event"]:
                    os.system("start" + " " + i["event"])
                elif os.path.exists(i["event"]):
                    os.startfile(filepath=i["event"])

        return 
        
    def start_tread(function):
        tread = threading.Thread(target=function)
        return tread
    
    def verify_modules():
        for i in data.modules:
            os.system(f"pip3 install {i}")
            tool.clear_screen()
        return
    
    def exit_program():
        exit()