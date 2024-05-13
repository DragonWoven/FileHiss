hasDepends = True
hasTksvg = True
hasTtkthemes = True
try: 
  import ttkthemes
except:
  print("ttkthemes isn't present, some themes may be missing")
  hasTtkthemes = False
try:
  import tkinter as tk
  from tkinter import ttk
except:
  hasDepends = False
  print("tkinter is missing!")
try:
  import tksvg
except:
  hasTksvg = False
  print("tksvg is missing!")
if not hasDepends:
  exit()
import FileManager.Settings as Settings
from FileManager.fileNav import *



root = tk.Tk()
root.title("File Manager")
currentStyle = Settings.getTheme()

#Loading Icons

if hasTksvg:
  tksvg.load(root)
  TrashIcon = tksvg.SvgImage(file = "assets/trash.svg")
  SettingsIcon = tksvg.SvgImage(file = "assets/settings.svg")
  FavIcon = tksvg.SvgImage(file = "assets/favorite.svg")




root.geometry("500x360")
root.minsize(500, 360)
#Style
style = ttk.Style()
if hasTtkthemes:
  ttkthemes.themed_style.ThemedStyle(theme=currentStyle)
else:
  style.theme_use(currentStyle)
root['bg'] = style.lookup(currentStyle, "background")
ManagerLabel = ttk.Label(text="File Manager")
ManagerLabel.pack()



#---Nav----
#Frame
navFrame = ttk.Frame(root)
navFrame.pack()
#Wigets
dirBox = ttk.Entry(navFrame)
dirBox.grid(column=0,row=0)
enterBtn = ttk.Button(navFrame, text="Enter", width=5, command=lambda: viewDir(dirBox.get()))
enterBtn.grid(column=1,row=0)
upDirBtn = ttk.Button(navFrame, text="^", width=2, command=lambda: upDir())
upDirBtn.grid(column=2,row=0)
if hasTksvg:
  settingsBtn = ttk.Button(navFrame, width=1, command=lambda: Settings.openSettings(root), image=SettingsIcon)
  trashsBtn = ttk.Button(navFrame, width=1, command=lambda: deleteSelected(), image=TrashIcon)
  FavBtn = ttk.Button(navFrame, width=1, command=lambda: addFav(), image=FavIcon)
else:
  settingsBtn = ttk.Button(navFrame, width=2, command=lambda: Settings.openSettings(root), text="S")
  trashsBtn = ttk.Button(navFrame, width=2, command=lambda: deleteSelected(), text="D")
  FavBtn = ttk.Button(navFrame, width=2, command=lambda: addFav(), text="F")

settingsBtn.grid(column=3,row=0)
trashsBtn.grid(column=4,row=0)
FavBtn.grid(column=5,row=0)

def addFav():
  Settings.addFavorite(getCurrentDir())
  UpdateFav(Settings.getFavorites())


#File View
baseFrame = ttk.Frame()
baseFrame.pack()

dirFrame = ttk.Frame(baseFrame)
dirFrame.pack()
dirView = ttk.Treeview(dirFrame,show="tree")
dirView.grid(row=0, column=2)
def doubleClick(event):
  selectedID = dirView.selection()
  data = dirView.item(selectedID,"text")
  chardir = list(getCurrentDir())
  if chardir[len(chardir)-1] == "/":
    newDir = getCurrentDir() + data
  else:
    newDir = getCurrentDir() + "/" + data
  viewDir(newDir)
dirView.bind("<Double-1>", doubleClick)







seperator = ttk.Frame(dirFrame, width=50)
seperator.grid(column=1,row=2)

FavView = ttk.Treeview(dirFrame,show="tree")
FavView.grid(row=0,column=0)

def FavClick(event):
  selectedID = FavView.selection()
  data = FavView.item(selectedID,"text")
  viewDir(Settings.getFavorites()[data])

FavView.bind("<Double-1>", FavClick)






def UpdateListBox(updatedList:list):
  dirView.delete(*dirView.get_children())
  for i in updatedList:
    dirView.insert('', tk.END, text=i)

def UpdateFav(updatedList:list):
  FavView.delete(*FavView.get_children())
  for i in updatedList:
    FavView.insert('', tk.END, text=i)


def viewDir(Dir):
  UpdateListBox(openDir(Dir))
  dirBox.delete(0,tk.END)
  dirBox.insert(0, Dir)


def upDir():
  newDir = getPrevDir(dirBox.get())
  viewDir(newDir)

def deleteSelected():
  selectedID = dirView.selection()
  selected = dirView.item(selectedID,"text")
  Dir = list(getCurrentDir())
  if Dir[len(Dir) - 1] == "/":
    rmdir = getCurrentDir() + selected
  else:
    rmdir = getCurrentDir() + "/" + selected
  delete(rmdir)
  viewDir(getCurrentDir())


for i in range(100):
    text = f"Item #{i+1}"
    dirView.insert("", "end", text=text)

viewDir(Settings.getDefaultDir())







UpdateFav(Settings.getFavorites())

root.mainloop()
