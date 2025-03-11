import tkinter
def textedit()
  text = input("")
def savefile():
  if tkinter.keysym = "ctrl+x":
    c1 = input("Save file?")
    if c1 = "y":
      fpath = input("Enter path to save file: ")
      with open(fpath, "w") as file:
        file.write(text)
def main():
  textedit()
  savefile()
main()
