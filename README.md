# Automating powershell-empire interaction via RESTful APIs
This repository contains a concise code example for automating access to the PowerShell Empire C2 framework via its REST API. Using the API, you can write Python scripts to perform various tasks such as:
- Creating listeners and agents.
- Executing arbitrary shell commands on all or specific agents.
- Scheduling periodic command execution and implementing other automation capabilities.

## Major Steps
### Run Empire in Server Mode
Ensure that Empire is running in server mode with the REST API enabled. The default port for the API is 13367.
### Generate an API Token
To access the API via Python, you need an authentication token. The [documentation]([url](https://github.com/EmpireProject/Empire/wiki/RESTful-API)) suggests a method for generating the token. However, if you encounter issues generating the token for remote REST API access, you can use Starkiller to log in and find the token from the page body, shown in the following photo.
![image](https://github.com/user-attachments/assets/b725e497-5a05-4cc8-b815-07dc8888c22b)


### Write Python Code
Use the Python requests library to interact with the Empire API and perform the desired operations.
