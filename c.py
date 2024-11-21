import os
print("-------------------------CONSOLE INITIATED-------------------------")
commands = {
    "help": "command that shows all commands.",
    "stop": "commands that stops the shell session.",
    "mdir": "makes a directory in your directory.",
    "dir": "shows your current directory.",
    "cd": "changes your directory",
    "ls": "list all directories.",
    "home": "brings you to where you started the shell.",
    "mfile": "makes a file and optionally writes something within.",
    "rmdir": "removes a directory.",
}
home = os.getcwd()
while True:
    c = input("$>")
    c = c.split(" ")
    if c[0] in commands.keys():
        if c[0] == "help":
            for key in commands.keys():
                print(key, end= ": ")
                print(commands.get(key))
        if c[0] == "stop":
            exit()
        if c[0] == "mdir":
            try:
                dir = os.getcwd()
                dirr = f"{dir}/{c[1]}"
                os.mkdir(dirr)
                print(f"{dirr} was made.")
            except:
                print("an error ocurred.")
        if c[0] == "dir":
            print(os.getcwd())   
        if c[0] == "cd":
            try:
                os.chdir(c[1])
            except:
                print("an error ocurred.") 
        if c[0] == "ls":
            try:
                for x in os.listdir(c[1]):
                    print(x, end= " ")
                print()
            except:
                for x in os.listdir(os.getcwd()):
                    print(x, end= " ")
                print()
        if c[0] == "home":
            os.chdir(home)
        if c[0] == "mfile":
            try:
                with open(os.path.join(os.getcwd(), c[1]), 'w', encoding="utf-8") as f:
                    try:
                        f.write(c[2])
                        print("file made.")
                    except:
                        print("file made.")
            except:
                print("command failed.")  
        if c[0] == "rmdir":
            try:
                try:
                    os.rmdir(c[1])
                    print("made directory")
                    
                except:
                    os.rmdir(os.path.join(os.getcwd(), c[1]))
                    print("made directory")
            except:
                print("command failed.")
            
    else:
        print("invalid command, use help for all commands.")

