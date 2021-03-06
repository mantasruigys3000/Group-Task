import os

"""
This program collects all usernames and passwords hidden in the L3 Folder and allows the user to pick the username
for which they want to see the passwords for
"""


passwords = {} #dictionary of passwords with the users as the key

def passSearch(lines,cPath):
    """
    function that takes list of lines from current open file
        :param lines: the current list of lines to search through 
        :param cPath: the path of the lines
    """
    for line in lines:

        if line.find("Username",0,len(line)) > -1: #if the line contains username a variable is formatted from it to get just the username
            uName = (line.split(" ")[1]) #removes the word username
            uName = uName[:-1] # removes line termination from the string

        if line.find("Password",0,len(line)) > -1: # if the line contains password then another string is formatted just like the username
            pName = (line.split(" ")[1])
            pName = pName[:-1]

            if uName in passwords.keys(): #checks to see if this user has already got a dictionary entry
                passwords[uName].append((pName,cPath)) # if so then add the found password to the list of passwords linked with the username
            else:
                passwords[uName] = [[pName,cPath]] #if the name is not already a key make it one by creating a list with a single element so it can later be appended too

print("Collecting Passwords...") # shows the program is working so the user does not think the program has crashed at the start

for root , dirs, files in os.walk("./L3"): # loops thorugh the entire folder of L3 where the passwords are hidden
    for name in files: #this loops through every found file that is not a directory

        fPath = str(root)+ "/" + str(name) # a filepath is created using the root and the file name

        if os.path.exists(fPath): # checks to see if the path can be accessed, should never return false as we created the file paths
            with open(fPath,"r") as text: 
                try:
                    passSearch(text.readlines(),fPath) # opens the file and passes through all the lines as a list into the passSearch function
                except Exception as e:
                    print("Error "+ str(e))



def printPasswords(key): 
    """
    macro for printing all passwords linked to a key
        :param key: the username that you want the passwords for
    """
    print("Passwords for user "+key+":\n")
    for p in passwords[key]:
        print("Password: "+str(p[0]))
        print("Location: "+str(p[1]) + "\n")
    
printPasswords("GailOllis")