from dataclasses import dataclass
import os

@dataclass
class data:
    Microfone_List_reported = []
    Microfone_Open = True
    Debug:bool = False
    modules = ["SpeechRecognition","googlesearch-python","PyAudio"]