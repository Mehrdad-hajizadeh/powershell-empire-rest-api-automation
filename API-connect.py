import requests
import json

# Empire REST API details
API_URL = "http://127.0.0.1:1337/api/v2"  # Replace with your Empire API endpoint

def list_listener (token):
    url =  f"{API_URL}/listeners"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        lst_list = response.json()
        print("[+] Listeners List:")
        for lst in lst_list['records']:
                #print(lst)
                print(f"ID: {lst['id']} Name: {lst['name']}, Template: {lst['template']}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching agents: {e}")

# Function to list agents (bots)
def list_agents(token):
    url = f"{API_URL}/agents"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        agents = response.json()
        print("[+] Agents List:")
        for agent in agents['records']:
            print(f"ID: {agent['ID']}, Name: {agent['name']}, Status: {agent['status']}")
      
if __name__ == "__main__":
    # Step 1: Authenticate and get token
    token = "" # put your token 
    if not token:
        exit(1)
    
    # Step 2: List agents
    list_listener(token)
