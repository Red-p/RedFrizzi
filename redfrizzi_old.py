import requests
import sys
import os
from dotenv import load_dotenv
import time

load_dotenv("env")
def do_get(url, headers,querystring):
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #return response.text
    return "pippo"

def print_file(data,filename):
    with open(filename,"a") as of:
        of.write(data)

def printLogo():
    #os.system("clear")
    print ("""


    $$$$$$$\                  $$\ $$$$$$$$\        $$\                     $$\ 
    $$  __$$\                 $$ |$$  _____|       \__|                    \__|
    $$ |  $$ | $$$$$$\   $$$$$$$ |$$ |    $$$$$$\  $$\ $$$$$$$$\ $$$$$$$$\ $$\ 
    $$$$$$$  |$$  __$$\ $$  __$$ |$$$$$\ $$  __$$\ $$ |\____$$  |\____$$  |$$ |
    $$  __$$< $$$$$$$$ |$$ /  $$ |$$  __|$$ |  \__|$$ |  $$$$ _/   $$$$ _/ $$ |
    $$ |  $$ |$$   ____|$$ |  $$ |$$ |   $$ |      $$ | $$  _/    $$  _/   $$ |
    $$ |  $$ |\$$$$$$$\ \$$$$$$$ |$$ |   $$ |      $$ |$$$$$$$$\ $$$$$$$$\ $$ |
    \__|  \__| \_______| \_______|\__|   \__|      \__|\________|\________|\__|
                                                                           
                                                                           
                                                                                                                                                                                                                               
  Reference //github
        """ )


if __name__ == "__main__":
    
    url=os.getenv('URL')
    base_querystring=  {"func":"auto"}
    headers = {
        "X-RapidAPI-Key": os.getenv('HEADERS_API_KEY'),
        "X-RapidAPI-Host": os.getenv('HEADERS_API_HOST')
    }
    printLogo()
    if(len(sys.argv) <=2):
        
        print("Options: [-h help] [-f file] [-t target]\n")
        
        exit()
    
    if(sys.argv[1] == "-t"):
        
        target= str(sys.argv[2])
        base_querystring["term"]= target
        print("CURRENT TARGET: " + target.upper())
        res=do_get(url,headers,base_querystring)
        if(len(sys.argv) > 3 and sys.argv[3]== "-o"):
            with open(sys.argv[4],"a") as of:
                of.write(target.upper())
                of.write(res)
            
        else:
            print(res)

        exit()    

    if(sys.argv[1] == "-f"):
        
        file_name_input= str(sys.argv[2])
        output_file=""
        out_ok=False
        out_file_pointer=None
        with open(file_name_input,"r") as file:

            if(len(sys.argv) > 3 and sys.argv[3] == "-o"):
                output_file=sys.argv[4]
                out_file_pointer=open(output_file,"a")
                out_ok=True
            
            for line in file:
                current_target= line.strip()
                base_querystring["term"]= current_target
                print("CURRENT TARGET: "+ current_target.upper())
                res=do_get(url,headers,base_querystring)
                if out_ok:
                    out_file_pointer.write(current_target.upper())
                    out_file_pointer.write(res)
                else:
                    
                    print(res)
                    
                time.sleep(1.2)
            if out_ok:
                out_file_pointer.close()
        exit()