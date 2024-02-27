import tkinter as tk
from tkinter import ttk
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
    defaultDirFrame = ttk.Frame(newWindow)
    defaultDirFrame.grid(row=1,column=0) 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Settings")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label = ttk.Label(newWindow, text ="Default Path")
    Label.grid(row=0,column=0)
    
    defaultDir = ttk.Entry(defaultDirFrame)
    defaultDir.delete(0,tk.END)
    defaultDir.insert(0,getDefaultDir())
    defaultDir.grid(row=1,column=2)

    ttk.Button(defaultDirFrame, text="Apply", command=lambda: setDefaultPath(defaultDir.get())).grid(row=0,column=3)
    defaultDir.grid(column=0,row=0)
