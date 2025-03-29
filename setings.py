from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtGui import QPixmap,QIcon,QFont
from data import data,Auto_Flow_UI
import speech_recognition as sr

class Setings(QWidget):
    def setings(app):
        try:
            setings_Window = Auto_Flow_UI.create_window(resX=data.resolutionX,resY=data.resolutionY,Logo_path="icon/TerminalLogo.ico")
            
            title = Auto_Flow_UI.create_text(txt="Setings",x=170,y= 40,screm= setings_Window)

            Commands_Control_BTN = Auto_Flow_UI.create_btn(txt=" Comandos De Voz",X= 140 , Y=100 , A=data.basicBtnAltura,L=data.basicBtnLarge,screm= setings_Window)
            Commands_Control_BTN.clicked.connect(Setings.list_micro(setings_Window=setings_Window))

            Mircrofone_List_BTN = Auto_Flow_UI.create_btn(txt=" Comandos De Voz",X= 140 , Y=80 , A=data.basicBtnAltura,L=data.basicBtnLarge,screm= setings_Window)


            setings_Window.show()
        except Exception as E:
            print(f"Erro Al Carregar Setings, Erro: {E}")


    def list_micro(setings_Window):
        list_micro = sr.Microphone().list_microphone_names()
        txt_list = Auto_Flow_UI.create_text(txt="Setings",x=170,y= 50,screm= setings_Window)
        data.Microfone_List_reported.append(list_micro)
        return