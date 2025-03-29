from dataclasses import dataclass
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtGui import QPixmap,QIcon,QFont
import os

@dataclass
class data:
    Microfone_List_reported = []
    Microfone_Open = True
    languege = "pt-BR"
    modules = ["SpeechRecognition","PyAudio"]
    Debug = True
    resolutionX = 500
    resolutionY = 500
    basicBtnLarge = 200
    basicBtnAltura = 35


class Auto_Flow_UI:
    def create_btn(screm, txt, X, Y, A, L):
        BTN = QPushButton(txt, screm)
        BTN.setGeometry(X, Y, L, A)
        BTN.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(
                    spread:pad,
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0078D4, stop:1 #005A9E
                );
                color: white;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
                padding: 8px 16px;
                border: 2px solid #005A9E;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #004578;
                color: #D1E8FF;
            }
        """)
        return BTN

    def create_text(screm, txt, x, y):
        Title = QLabel(txt, screm)
        Title.move(x, y)
        Title.setStyleSheet("""
            QLabel {
                color: #eaeaea;
                font-size: 24px;
                font-weight: bold;
                background-color: transparent;
            }
        """)
        return Title

    def create_window(resX, resY, Logo_path):
        Window = QWidget()
        Window.resize(resX, resY)
        Window.setWindowTitle("Auto Flow")
        Window.setWindowIcon(QIcon(Logo_path))
        Window.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-radius: 12px;
            }
        """)
        return Window