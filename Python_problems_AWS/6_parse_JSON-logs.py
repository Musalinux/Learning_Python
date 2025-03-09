"""
Parse JSON logs and extract specifi information
"""

import json

def extract_logs(log_file):
    with open (log_file, 'r') as file:
        logs = json.load(file) # load json data from log_file
        
    errors = [log for log in logs if log['level'] == 'ERROR'] # filter logs with ERRORS and return it. 
    return errors

errors = extract_logs('/var/logs/my_app.log') # Feed log file to function
for error in errors:
    print (error)