import tkinter as tk
import json 
from os import path

if not path.exists("settings.json"):
    settingsfile = open("settings.json", "w")
    settingsData = {
        "defaultDir": "/"
    }
    jsonSettings = json.dumps(settingsData)
    settingsfile.write(jsonSettings)
    settingsfile.close()


#main = tk.Tk()
#ain.geometry("250x250")
def getDefaultDir():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["defaultDir"]


def setDefaultPath(path):
    settingsData = {}
    with open("settings.json","r") as settingsFile:
        settingsData = json.load(settingsFile)
    settingsData["defaultDir"] = path
    with open("settings.json","w") as settingsFileW:
        jsonData = json.dumps(settingsData)
        settingsFileW.write(jsonData)


