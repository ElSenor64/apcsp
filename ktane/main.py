from SimpleWires import wires
from Buttons import button

print(" ____  _     _       _   _     _  ___                   ")
print("|  _ \| |__ | | __ _| |_| |_  | |/ / |_ __ _ _ __   ___ ")
print("| |_) | '_ \| |/ _` | __| __| | ' /| __/ _` | '_ \ / _ \\")
print("|  __/| | | | | (_| | |_| |_  | . \| || (_| | | | |  __/")
print("|_|   |_| |_|_|\__,_|\__|\__| |_|\_\\\\__\__,_|_| |_|\___|")
print("")

def promptKey():
  print("Enter the module you want to run or \"exit\". Run \"help\" to see this again.")
  print("| Modules | Command | Comment |")
  print("| ----------- | -------------- | -------------- |")
  print("| Simple Wires | wires | On the Subject of Wires |")
  print("| The Button | button | On the Subject of The Button |")
  print("| Simon Says | simon | On the Subject of Simon Says |")
  print("| Memory | memory | On the Subject of Memory |")
  print("")

promptKey()
command = str(raw_input("[ktane@PhlattKtane ~]$ ")).lower()
#print(command)

while True:
  #promptKey()
  #command = str(raw_input("[ktane@PhlattKtane ~]$ ")).lower()
  #print("THE COMMAND IS CURRENTLY: " + command)
  if(command == "exit"):
    print("")
    print("See you later!")
    print("BOOOM!!!")
    print("")
    exit()
    command = ""
  elif (command == "help"):
    print("")
    promptKey()
    command = ""
  elif (command == "wires"):
    print("")
    wires()
    command = ""
  elif (command == "button"):
    print("")
    button()
    command = ""
  elif (command == "simon"):
    print("")
    simon()
    command = ""
  elif (command == "memory"):
    print("")
    memory()
    command = ""
  else:
    command = str(raw_input("[ktane@PhlattKtane ~]$ ")).lower()


#button()

#print(wires(["b", "B", "y"]))
