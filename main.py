import requests
import os

x = "https://discord.com/api/v9/users/@me"

def sexy(token):
    ex = {
        "Authorization": f"Bot {token}"
    }
    nothing = requests.get(x, headers=ex)
    if nothing.status_code == 200:
        gay = nothing.json()
        return gay
    else:
        return None

def no():
    slave = input("Enter Discord Bot Token: ")
    gay = sexy(slave)
    if gay:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Bot Name: {gay['username']}#{gay['discriminator']}")
        print(f"Bot ID: {gay['id']}")
    else:
        print("Invalid token")

if __name__ == "__main__":
    no()
