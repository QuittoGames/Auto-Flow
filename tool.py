import os
import platform
from dataclasses import dataclass
from data import data
from command import comamnds
import speech_recognition as sr
import subprocess
import asyncio
import sys
from time import sleep
import threading

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "modules", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)

            #Teste De Novo metodo de instaçao de modulos
            # for module in data.modules:
            #     try:
            #         __import__(module)
            #     except ImportError:
            #         subprocess.run([sys.executable, "-m", "pip", "install", module])
            # return
        
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
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
        
    start_tread = lambda func: threading.Thread(target=func)