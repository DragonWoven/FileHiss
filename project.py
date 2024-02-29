hasDepends = True
hasTksvg = True
import ttkthemes
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
import Settings
from fileNav import *

currentStyle = Settings.getTheme()
print(tk.TkVersion)

root = tk.Tk()
root.title("File Manager")
tksvg.load(root)
#Loading Icons
if hasTksvg:
  TrashIcon = tksvg.SvgImage(file = "assets/trash.svg")
  SettingsIcon = tksvg.SvgImage(file = "assets/settings.svg")




root.geometry("350x350")
#Style
style = ttk.Style()
ttkthemes.themed_style.ThemedStyle(theme=currentStyle)
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
upDirBtn = ttk.Button(navFrame, text="^", width=1, command=lambda: upDir())
upDirBtn.grid(column=2,row=0)
if hasTksvg:
  settingsBtn = ttk.Button(navFrame, width=1, command=lambda: Settings.openSettings(root), image=SettingsIcon)
  trashsBtn = ttk.Button(navFrame, width=1, command=lambda: deleteSelected(), image=TrashIcon)
else:
  settingsBtn = ttk.Button(navFrame, width=1, command=lambda: Settings.openSettings(root), text="T")
  trashsBtn = ttk.Button(navFrame, width=1, command=lambda: deleteSelected(), text="D")

settingsBtn.grid(column=3,row=0)
trashsBtn.grid(column=4,row=0)


#File View
baseFrame = ttk.Frame()
baseFrame.pack()

dirView = ttk.Treeview(baseFrame,show="tree")
dirView.pack()
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




def UpdateListBox(updatedList:list):
  dirView.delete(*dirView.get_children())
  for i in updatedList:
    dirView.insert('', tk.END, text=i)
  


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









root.mainloop()
