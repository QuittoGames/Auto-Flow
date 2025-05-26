from tool import tool
from data import data
import sys
from time import sleep

import speech_recognition as sr
import subprocess
import threading
import asyncio

data_local = data()

class Main():
    async def voice_command():
        rec = sr.Recognizer()   
        rec.adjust_for_ambient_noise(mic)
        tool.clear_screen()
        print("Micrfone Started")
        while data.Microfone_Open:
            try:
                with sr.Microphone(0) as mic:
                    print("Waining Audio ")  
                    audio = rec.listen(mic)
                    command = rec.recognize_google(audio, language=data.languege)
                    if str(command).lower().strip() == "fechar":return
                    tool.start_command(command)
                    print("Promt: "+ command)
            except Exception as E:
                print(f"Errro No Loop De Aldio, Erro: {E}")
                Main.voice_command()
                return

if __name__ == "__main__":
    if not data_local.Debug: asyncio.create_task(tool.verify_modules())
    asyncio.create_task(Main.voice_command())

    


