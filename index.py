from tool import tool
from data import data,Auto_Flow_UI
import sys
from time import sleep
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap,QIcon,QFont
from setings import Setings
import speech_recognition as sr
import threading
import asyncio

app = QApplication(sys.argv)
class MainProgram(QWidget):
    def Start():
        tool.clear_screen()
        try:
            
            StartUI = Auto_Flow_UI.create_window(resX=data.resolutionX,resY=data.resolutionY,Logo_path="icon/TerminalLogo.ico")
            
            Title = Auto_Flow_UI.create_text(screm= StartUI,txt = "Auto Flow",x= 170,y= 40)

            SetingsBTN = Auto_Flow_UI.create_btn(screm= StartUI,txt="Setings",X=140,Y=100,L= data.basicBtnLarge, A= data.basicBtnAltura)
            SetingsBTN.clicked.connect(lambda: Setings.setings(app=app))

            StartBTN = Auto_Flow_UI.create_btn(screm= StartUI,txt="Start",X=140,Y=150,L= data.basicBtnLarge, A= data.basicBtnAltura)
            StartBTN.clicked.connect(lambda: tool.start_tread(VoiceController.voice_command))

            exitBTN = Auto_Flow_UI.create_btn(screm=StartUI,txt="Exit",X=140,Y = 200, L= data.basicBtnLarge, A= data.basicBtnAltura)
            exitBTN.clicked.connect(tool.exit_program)
            #exitBTN.show()
            StartUI.show()
        except Exception as E:
            print(f"Erro Al Inicar Interface, Erro: {E}")
            return
        app.exec()

class VoiceController(QThread):
    def voice_command():
        rec = sr.Recognizer()   
        tool.clear_screen()
        print("Micrfone Started")
        while data.Microfone_Open:
            try:
                with sr.Microphone(0) as mic:
                    rec.adjust_for_ambient_noise(mic)
                    print("Waining Audio ")  
                    audio = rec.listen(mic)
                    command = rec.recognize_google(audio, language=data.languege)
                    if str(command).lower().strip() == "fechar":return
                    tool.start_command(command)
                    print("Promt: "+ command)
            except Exception as E:
                print(f"Errro No Loop De Aldio, Erro: {E}")
                VoiceController.voice_command()
                return

if __name__ == "__main__":
    Verify_tread = tool.start_tread(tool.verify_modules()).start()
    #MainProgram.Start() #Satrt UI
    #asyncio.run(VoiceController.voice_command())
    #PyQt6_thread = tool.start_tread(MainProgram.Start()).start()
    vocie_tread = tool.start_tread(VoiceController.voice_command()).start()


