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

def openSettings(rootWindow):
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(rootWindow)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    tk.Label(newWindow, 
          text ="Default Path").pack()
    defaultDir = tk.Entry(newWindow)
    defaultDir.delete(0,tk.END)
    defaultDir.insert(0,getDefaultDir())

    tk.Button(newWindow, text="Apply", command=lambda: setDefaultPath(defaultDir.get())).pack()
    defaultDir.pack()
