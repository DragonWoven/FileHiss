import os
from shutil import rmtree
import subprocess
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

def getFile(Dir):
  character = list(Dir)
  endsWithSlash = False
  if len(character) <= 1:
    return "/"
  pos = len(character) -1
  if character[pos] == "/":
    pos -= 1
    endsWithSlash = True
  
  
  done = False
  file = ""
  while not done:
    if character[pos] == "/":
      done = True
    else:
      pos -= 1
  pos += 1
  length = len(character)
  if endsWithSlash:
    length -= 1

  while pos != length:
    file += character[pos]
    pos += 1
  return file

def getFileExtension(File):
  characters = list(File)
  pos = len(characters) -1
  extension = ""
  while characters[pos] != ".":
    pos -=1
  while pos != len(characters):
    extension += characters[pos]
    pos += 1
  return extension
    

  


def runFile(Dir):
  if os.path.isfile(Dir):
    if getFileExtension(getFile(Dir)) == ".exe":
      subprocess.Popen(Dir)
  else:
    raise ValueError("File doesn't exits")

print(getFileExtension(getFile("assets/trash.svg")))