# Read the file
# store data in a variable -> list
# open file in write mode
# updating max_connections -> if condition used

def update_server_config (file_path, key, value):

    with open (file_path, "r") as file:
        lines = file.readlines()
    
    with open (file_path, "w") as file:
        for line in lines: 
            if key in line: 
                file.write (key + " " + "=" + " " + value + "\n")
            else:
                file.write (line)

update_server_config ("server.conf", "MAX_CONNECTIONS", "300")