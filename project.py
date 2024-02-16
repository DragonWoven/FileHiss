hasDepends = True
try:
  import tkinter as tk
except:
  hasDepends = False
  print("tkinter is missing!")
try:
  import tksvg
except:
  hasDepends = False
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
    pass

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


def openSettings():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(gui)
 
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
    defaultDir.insert(0,Settings.getDefaultDir())

    tk.Button(newWindow, text="Apply", command=lambda: Settings.setDefaultPath(defaultDir.get())).pack()
    defaultDir.pack()
    



upButton = tk.Button(gui,text="^", command=lambda: upDir(getCurrentDir()))
delButton = tk.Button(gui, text="D", command=delCurrent, image=TrashIcon)
settingsButton = tk.Button(gui, text="D", command=openSettings, image=SettingsIcon)
text.grid(column=1,row=1) 



dirbox.grid(column=1,row=0)
enterButton.grid(column=2,row=0)
upButton.grid(column=3,row=0)
delButton.grid(column=4,row=0)
settingsButton.grid(column=5,row=0)


gui.geometry("230x240")
dirbox.delete(0,tk.END)
dirbox.insert(0,getCurrentDir())
# openDir(defaultdir)
viewDir(getCurrentDir())



gui.mainloop()