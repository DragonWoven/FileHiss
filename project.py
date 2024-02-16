import tkinter as tk
import os
from subprocess import run
from shutil import rmtree
import tksvg
import Settings
from fileNav import *





gui = tk.Tk()
gui.title("File Manager")
dirbox = tk.Entry(gui)
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
  UpdateListBox(openDir(Dir))
  print(currentDir)

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



enterButton = tk.Button(gui,text="Enter",command=lambda: viewDir(dirbox.get()) ,anchor=tk.N)

def upDir(Dir):
  newDir = getPrevDir(Dir)
  dirbox.delete(0,tk.END)
  dirbox.insert(0,newDir)
  viewDir(newDir)

def delMode():
  selected = lsbox.get(tk.ACTIVE)
  dir = list(indir)
  if dir[len(dir) -1 == "/"]:
    rmdir = indir + selected
  else:

    rmdir = indir + "/" + selected
  if os.path.isdir(rmdir):

    rmtree(dir + "/" + selected)
    openDir(dir)
  else:
    os.remove(rmdir)

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
delButton = tk.Button(gui, text="D", command=delMode, image=TrashIcon)
settingsButton = tk.Button(gui, text="D", command=openSettings, image=SettingsIcon)
text.grid(column=1,row=1) 



dirbox.grid(column=1,row=0)
enterButton.grid(column=2,row=0)
upButton.grid(column=3,row=0)
delButton.grid(column=4,row=0)
settingsButton.grid(column=5,row=0)


gui.geometry("270x250")
dirbox.delete(0,tk.END)
dirbox.insert(0,getCurrentDir())
# openDir(defaultdir)
viewDir(getCurrentDir())



gui.mainloop()