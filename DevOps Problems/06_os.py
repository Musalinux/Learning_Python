import os 

folders = input ("Please input the names of the folders with spaces in between: ").split()

for folder in folders: 
    try: 
        files = os.listdir(folder)
    except FileNotFoundError: 
        print (f"Please enter a valid folder name, the folder '{folder}' does not exist")
        continue 

    print ("===== Listing files for the folder " + folder) 

    for file in files:
        print (file)