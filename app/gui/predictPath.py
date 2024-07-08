from tkinter import *
import os
import platform

class PredictPath:
    def getArduinoPath(self, status_label_prediction: Label, hardware: str):
        curPlatform = platform.system()
        detectedPlatform = TRUE

        if (curPlatform == 'Darwin'): # MacOS
            path = os.path.expanduser("~") + "/Documents/Arduino/libraries/" + hardware
        elif (curPlatform == 'Windows'):
            path = os.path.expanduser("~") + "/OneDrive/Documents/Arduino/libraries/" + hardware
        elif (curPlatform == 'Linux'):
            path = os.path.expanduser("~") + "/Arduino/libraries/" + hardware
        else:
            detectedPlatform = FALSE
            path = os.path.expanduser("~") + "/Arduino/libraries/" + hardware

        if (detectedPlatform == TRUE):
            status_label_prediction.config(text=f"Platform identified: {curPlatform}", fg="green")
        else:
            status_label_prediction.config(text=f"Platform unidentified: {curPlatform}\nProgram may not work as expected", fg="red")
        return path