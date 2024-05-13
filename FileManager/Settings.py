import tkinter as tk
from tkinter import ttk
import json 
from os import path
from FileManager.fileNav import getFile
ttkthemesPresent = True
try:
    import ttkthemes
except:
    ttkthemesPresent = False


def getTheme():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["theme"]


themes = ["classic", "default", "clam", "alt"]
#externalThemes = ["breeze", "awdark", "blue", "winxpblue", "ubuntu", "arc","clearlooks", "equilux", "itft1", "elegance","keramilk",]
externalThemes = []   
root = ""
if ttkthemesPresent:
    print("ttkthemes presnt")
    ttkthemes.ThemedStyle.pixmap_themes.append("breeze")
    externalThemes = ttkthemes.ThemedStyle.pixmap_themes
    for i in externalThemes:
        themes.append(i)
        
else:
    if not getTheme() in themes:
        setTheme("clam")
    

if not path.exists("settings.json"):
    defaultTheme = "clam"
    if ttkthemesPresent:
        defaultTheme = "breeze"
    settingsfile = open("settings.json", "w")
    settingsData = {
        "defaultDir": "/",
        "theme" : defaultTheme,
        "favorites": {}
    }
    jsonSettings = json.dumps(settingsData)
    settingsfile.write(jsonSettings)
    settingsfile.close()


#main = tk.Tk()
#ain.geometry("250x250")
def getDefaultDir():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["defaultDir"]


def getFavorites():
    with open("settings.json","r") as settingsFile:
        return json.load(settingsFile)["favorites"]

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
    if ttkthemesPresent:
        ttkthemes.themed_style.ThemedStyle(theme=theme)



def addFavorite(Dir):
    settingsData = {}
    with open("settings.json","r") as settingsFile:
        settingsData = json.load(settingsFile)
    settingsData["favorites"][getFile(Dir)] = Dir
    with open("settings.json","w") as settingsFileW:
        jsonData = json.dumps(settingsData)
        settingsFileW.write(jsonData)


def openSettings(root):
    currentTheme = getTheme()
    
    #Creating Window
    newWindow = tk.Toplevel(root)
    newWindow.title("Settings")
    #Default Directory
    defaultDirFrame = ttk.Frame(newWindow)
    defaultDirFrame.grid(row=1,column=0)
    defaultDir = ttk.Entry(defaultDirFrame)
    defaultDir.delete(0,tk.END)
    defaultDir.insert(0,getDefaultDir())
    defaultDir.grid(row=1,column=2)
    DefaultDirLbl = ttk.Label(newWindow, text ="Default Path")
    DefaultDirLbl.grid(row=0,column=0)
    ttk.Button(defaultDirFrame, text="Apply", command=lambda: setDefaultPath(defaultDir.get())).grid(row=0,column=3)
    #Changing Theme
    
    
    themeFrame = ttk.Frame(newWindow)
    themeLbl = ttk.Label(themeFrame, text="Theme")
    themeLbl.grid(row=0,column=0)
    themeFrame.grid(row=2,column=0)
    style = ttk.Style()
    newWindow['bg'] = style.lookup(currentTheme, "background")
    theme = tk.StringVar(themeFrame)
    theme.set(currentTheme)
    def applyTheme(theme, style):
        if not ttkthemesPresent:
            style.theme_use(theme)
        setTheme(theme)
        root['bg'] = style.lookup(theme, "background")
        newWindow['bg'] = style.lookup(theme, "background")


    themeMenu = ttk.OptionMenu(themeFrame, theme, currentTheme, *themes)
    themeMenu.grid(row=3,column=0)
    applyThemeBtn = ttk.Button(themeFrame, text="Apply", command=lambda: applyTheme(theme.get(), style))
    applyThemeBtn.grid(row=3,column=2)
 
    # sets the geometry of toplevel
    newWindow.geometry("255x255")
    newWindow.minsize(255, 255)
    # A Label widget to show in toplevel
    
    
    
    defaultDir.grid(column=0,row=0)
    
