hasDepends = True
hasTksvg = True
try:
  import tkinter as tk
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
from subprocess import run
import Settings
from fileNav import *





gui = tk.Tk()
gui.minsize(230, 240)
navFrame = tk.Frame(gui)
navFrame.grid(row=0, column=1, sticky=tk.W+tk.E)
gui.title("File Manager")
dirbox = tk.Entry(navFrame)
currentDirButtons = []
sb = tk.Scrollbar(gui)
sb.grid(row=2, column=1,  sticky='e')
lsbox = tk.Listbox(gui,height=10,width=20, yscrollcommand = sb.set)
lsbox.grid(row=2,column=1,padx=20,pady=20)
if hasTksvg:
  TrashIcon = tksvg.SvgImage(file = "assets/trash.svg")
  SettingsIcon = tksvg.SvgImage(file = "assets/settings.svg")
text = tk.Label(text="File Manager")
setCurrentDir(Settings.getDefaultDir())

def UpdateListBox(updatedList:list):
  lsbox.delete(0,tk.END)
  for i in updatedList:
    lsbox.insert(tk.END,i)
  
def viewDir(Dir):
  try:
    UpdateListBox(openDir(Dir))
  except:
    runFile(Dir)

previousClick = ""
def onClick(event):
  global previousClick
  selection = event.widget.curselection()
  if selection:
    index = selection[0]
    data = event.widget.get(index)
    if previousClick == data:
      chardir = list(getCurrentDir())
      if chardir[len(chardir)-1] == "/":
        newDir = getCurrentDir() + data
      else:
        newDir = getCurrentDir() + "/" + data
      viewDir(newDir)
      previousClick = ""
      dirbox.delete(0, tk.END)
      dirbox.insert(0, newDir)
    else:
      previousClick = data





lsbox.bind("<<ListboxSelect>>", onClick)

def confirm(event):
  viewDir(dirbox.get())

gui.bind('<Return>', confirm)



enterButton = tk.Button(navFrame,text="Enter",command=lambda: viewDir(dirbox.get()) ,anchor=tk.N,)

def upDir(Dir):
  newDir = getPrevDir(Dir)
  dirbox.delete(0,tk.END)
  dirbox.insert(0,newDir)
  viewDir(newDir)

def delCurrent():
  selected = lsbox.get(tk.ACTIVE)
  Dir = list(getCurrentDir())
  if Dir[len(Dir) - 1] == "/":
    rmdir = getCurrentDir() + selected
  else:
    rmdir = getCurrentDir() + "/" + selected
  delete(rmdir)
  viewDir(getCurrentDir())


upButton = tk.Button(navFrame,text="^", command=lambda: upDir(getCurrentDir()))
if hasTksvg:
  
  delButton = tk.Button(navFrame, text="D", command=delCurrent, image=TrashIcon)
  settingsButton = tk.Button(navFrame, text="D", command=lambda: Settings.openSettings(gui), image=SettingsIcon)
else:
  delButton = tk.Button(navFrame, text="D", command=delCurrent)
  settingsButton = tk.Button(navFrame, text="S", command=lambda: Settings.openSettings(gui))

text.grid(column=1,row=1) 



dirbox.grid(column=1,row=0, sticky=tk.W+tk.E)
enterButton.grid(column=2,row=0, sticky=tk.W+tk.E)
upButton.grid(column=3,row=0, sticky=tk.W+tk.E)
delButton.grid(column=4,row=0, sticky=tk.W+tk.E)
settingsButton.grid(column=5,row=0, sticky=tk.W+tk.E)


gui.geometry("230x240")
dirbox.delete(0,tk.END)
dirbox.insert(0,getCurrentDir())
viewDir(getCurrentDir())



gui.mainloop()