import tkinter as tk
from tkinter import ttk
import json 
from os import path
import ttkthemes
themes = ["classic", "default", "clam", "alt"]
externalThemes = ["breeze", "awdark", "blue", "winxpblue", "ubuntu"]
root = ""
def start(rootwin,hasTtkthemes):
    root = rootwin
    if hasTtkthemes:
        for i in externalThemes:
            themes.append(i)
    else:
        if not getTheme() in themes:
            setTheme("clam")

if not path.exists("settings.json"):
    settingsfile = open("settings.json", "w")
    settingsData = {
        "defaultDir": "/",
        "theme" : "clam"
    }
    jsonSettings = json.dumps(settingsData)
    settingsfile.write(jsonSettings)
    settingsfile.close()


#main = tk.Tk()
#ain.geometry("250x250")
def getDefaultDir():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["defaultDir"]

def getTheme():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["theme"]
currentTheme = getTheme()


def setDefaultPath(path):
    settingsData = {}
    with open("settings.json","r") as settingsFile:
        settingsData = json.load(settingsFile)
    settingsData["defaultDir"] = path
    with open("settings.json","w") as settingsFileW:
        jsonData = json.dumps(settingsData)
        settingsFileW.write(jsonData)
def setTheme(theme):
    settingsData = {}
    with open("settings.json","r") as settingsFile:
        settingsData = json.load(settingsFile)
    settingsData["theme"] = theme
    with open("settings.json","w") as settingsFileW:
        jsonData = json.dumps(settingsData)
        settingsFileW.write(jsonData)
    ttkthemes.themed_style.ThemedStyle(theme=theme)
    

def openSettings(rootWindow):
    
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(rootWindow)
    defaultDirFrame = ttk.Frame(newWindow)
    defaultDirFrame.grid(row=1,column=0)
    themeFrame = ttk.Frame(newWindow)
    themeFrame.grid(row=2,column=0)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Settings")

    style = ttk.Style()
    newWindow['bg'] = style.lookup(currentTheme, "background")

    
    theme = tk.StringVar(themeFrame)
    theme.set(currentTheme)
    def applyTheme(theme, style):
        setTheme(theme)
        rootWindow['bg'] = style.lookup(theme, "background")
        newWindow['bg'] = style.lookup(theme, "background")


    themeMenu = ttk.OptionMenu(themeFrame, theme, currentTheme, *themes)
    applyThemeBtn = ttk.Button(themeFrame, text="Apply", command=lambda: applyTheme(theme.get(), style))
    applyThemeBtn.grid(row=0,column=3)
 
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
    themeMenu.grid(column=0,row=0)
