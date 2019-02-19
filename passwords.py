import os

passwords = {}

def passSearch(lines):
    for line in lines:
        if line.find("Username",0,len(line)) > -1:
            uName = (line.split(" ")[1])
            uName = uName[:-1]
        if line.find("Password",0,len(line)) > -1:
            pName = (line.split(" ")[1])
            pName = pName[:-1]
            if uName in passwords.keys():
                passwords[uName].append(pName)
            else:
                passwords[uName] = [pName]

print("Collecting Passwords...")
for root , dirs, files in os.walk("./L3"):
    for name in files:
        fPath = str(root)+ "/" + str(name)
        #print(fPath)
        if os.path.exists(fPath):
            with open(fPath,"r") as text:
                try:
                    passSearch(text.readlines())
                except Exception as e:
                    print("Error "+ str(e))



def printPasswords(key):
    print("Passwords for user "+key+":\n"+str(passwords[key]))
    
print("Welcome to the password database, below are a list of users\ninput the user you wish to see the passwords of")
for k in passwords.keys():
    print(k)
inputName = ""
while (inputName != "exit"):
    inputName = input()
    if inputName in passwords.keys():
        printPasswords(inputName)
    elif inputName != "exit":
        print("User "+inputName+" not detected")

print("\nProgram Exiting..")