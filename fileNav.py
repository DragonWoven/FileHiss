import os
from shutil import rmtree
currentDir = "/"
def setCurrentDir(Dir):
  global currentDir
  currentDir = Dir



def getPrevDir(Dir):
  character = list(Dir)
  if len(character) <= 1:
    return "/"
  pos = len(character) -1
  if character[pos] == "/":
    pos -= 1
  
  
  done = False
  
  while not done:
    if character[pos] == "/":
      done = True
    else:
      pos -= 1
  newDir = ""
  x = 0
  while x != pos:
    newDir += character[x]
    x+=1
  if newDir == "":
    return "/"
  else:
    return newDir

def getCurrentDir():
  global currentDir
  return currentDir
def filesInDir(Dir:str):
  files = []
  scan = []
  try:
      scan = os.scandir(Dir)
  except:
      raise ValueError("Not a Directory")
  for i in scan:
      files.append(i.name)
  return files

def openDir(Dir):
  if os.path.isdir(Dir):
    files = filesInDir(Dir)
    global currentDir
    setCurrentDir(Dir)
    return files
  else:
    raise ValueError("Not A Directory")
    

def delete(Dir):
  if os.path.isdir(Dir):
    rmtree(dir + "/" + selected)
  else:
    os.remove(Dir)

