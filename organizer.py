# Goal is automate the process of organizing my downloads folder by file extension

import os

currentUser = os.getlogin()

folderPath = 'C:\\Users\\' + currentUser + '\\Downloads'

listOfFiles = os.listdir(folderPath)

# Check to see what types of extensions there are and adds them to a list
listOfExtensions = []
for file in listOfFiles:
    extension = os.path.splitext(file)[1]
    listOfExtensions.append(extension)

# Create directories based on extentions
# Will need to remove duplicates from list so I don't create duplcate folders.
# After searching, converting the list into a set will remove duplicate values

noDuplicateExtentionsList = list(set(listOfExtensions))

# Now to create folders based off the this list
for ext in noDuplicateExtentionsList:
    try:
        os.mkdir(folderPath + "\\" + "Test" + ext)
    except:
        print("There is a directory that exist with the name: " + ext)


# Now to add the files to their respective folders
# First, have to check if a file or folder
# Then rename path name to new path name based on the ext
for file in listOfFiles:
    if os.path.isfile(folderPath + "\\" + file):
        try:
            os.rename(folderPath + "\\" + file, folderPath + "\\" + "Test" + os.path.splitext(file)[1] + "\\" + file)
        except:
            print("Not able to move file to respective folder")

# I believe I am done now.

