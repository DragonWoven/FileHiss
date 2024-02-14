def getPrevDir(Dir):
  character = list(Dir)
  pos = len(character) -1
  done = False
  
  while not done:
    if character[pos] == "/":
      pos
      done = True
    else:
      pos -= 1
  newDir = ""
  x = 0
  while x != pos:
    newDir += character[x]
    x+=1
  return newDir


  def filesInDir(dir:str):
    files = []
    try:
        scan = os.scandir(dir)
    except:
        ValueError("Not a Directory")
    for i in scan:
        files.append(i.name)
    return files

    def openDir(dir):
        files = filesInDir()