import os

passwords = {} #dictionary of passwords with the users as the key

def passSearch(lines): # function that takes list of lines from current open file
    for line in lines:

        if line.find("Username",0,len(line)) > -1: #if the line contains username a variable is formatted from it to get just the username
            uName = (line.split(" ")[1]) #removes the word username
            uName = uName[:-1] # removes line termination from the string

        if line.find("Password",0,len(line)) > -1: # if the line contains password then another string is formatted just like the username
            pName = (line.split(" ")[1])
            pName = pName[:-1]

            if uName in passwords.keys(): #checks to see if this user has already got a dictionary entry
                passwords[uName].append(pName) # if so then add the found password to the list of passwords linked with the username
            else:
                passwords[uName] = [pName] #if the name is not already a key make it one by creating a list with a single element so it can later be appended too

print("Collecting Passwords...") # shows the program is working so the user does not think the program has crashed at the start

for root , dirs, files in os.walk("./L3"): # loops thorugh the entire folder of L3 where the passwords are hidden
    for name in files: #this loops through every found file that is not a directory

        fPath = str(root)+ "/" + str(name) # a filepath is created using the root and the file name

        if os.path.exists(fPath): # checks to see if the path can be accessed, should never return false as we created the file paths
            with open(fPath,"r") as text: 
                try:
                    passSearch(text.readlines()) # opens the file and passes through all the lines as a list into the passSearch function
                except Exception as e:
                    print("Error "+ str(e))



def printPasswords(key): # macro for printing all passwords linked to a key
    print("Passwords for user "+key+":\n"+str(passwords[key]))
    
print("Welcome to the password database, below are a list of users\ninput the user you wish to see the passwords of\nWrite exit to quit\n") #user prompt

for k in passwords.keys(): # loop through every key in the dictionary and print it to give a list of users
    print(k)

inputName = "" #black string in order to start the loop

while (inputName != "exit"):

    inputName = input() # takes user input

    if inputName in passwords.keys(): # checks if input value matches a key in the passwords dictionary 
        printPasswords(inputName)
    elif inputName != "exit":
        print("User "+inputName+" not detected")

print("\nProgram Exiting..")