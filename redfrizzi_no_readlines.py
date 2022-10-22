import requests
import sys
import os
from dotenv import load_dotenv
import time
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import clear
from termcolor import *
import colorama
import json
import random
from johnparser import JohnParser
import time

def printLogo():
    #os.system("clear")
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    color=random.choice(colors)
    cprint("""


    $$$$$$$\                  $$\ $$$$$$$$\        $$\                     $$\ 
    $$  __$$\                 $$ |$$  _____|       \__|                    \__|
    $$ |  $$ | $$$$$$\   $$$$$$$ |$$ |    $$$$$$\  $$\ $$$$$$$$\ $$$$$$$$\ $$\ 
    $$$$$$$  |$$  __$$\ $$  __$$ |$$$$$\ $$  __$$\ $$ |\____$$  |\____$$  |$$ |
    $$  __$$< $$$$$$$$ |$$ /  $$ |$$  __|$$ |  \__|$$ |  $$$$ _/   $$$$ _/ $$ |
    $$ |  $$ |$$   ____|$$ |  $$ |$$ |   $$ |      $$ | $$  _/    $$  _/   $$ |
    $$ |  $$ |\$$$$$$$\ \$$$$$$$ |$$ |   $$ |      $$ |$$$$$$$$\ $$$$$$$$\ $$ |
    \__|  \__| \_______| \_______|\__|   \__|      \__|\________|\________|\__|
                                                                        
                                                                        
                                                                                                                                                                                                                            
Reference //github
        """,color) 

def do_get(url, headers,querystring):
    print("[+] entering do get")
    print("URL_: " +str(url))
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
    
## options --init
def init():
    api_key=input(" Enter API KEY:")
    print("[+] writing "+ api_key + " to env")
    with open ("env","w") as of:
        of.write("URL=\"https://breachdirectory.p.rapidapi.com/\"")
        of.write('\n')
        of.write("HEADERS_API_HOST=\"breachdirectory.p.rapidapi.com\"")
        of.write('\n')
        of.write("HEADERS_API_KEY="+ "\"" + api_key + "\"")
        of.write('\n')


def write_res_query(target,outputfile,result_query):
    res_asjson=dict()
    res_asjson["name"]= target.upper()
    res_asjson.update(json.loads(result_query))
    outputfile.write(json.dumps(res_asjson,indent=4))

def main():
    colorama.init()
    printLogo()
    user_input=""
    load_dotenv("env")
    url=os.getenv('URL')
    base_querystring=  {"func":"auto"}
    headers = {
        "X-RapidAPI-Key": os.getenv('HEADERS_API_KEY'),
        "X-RapidAPI-Host": os.getenv('HEADERS_API_HOST')
    }

    history = FileHistory("history_file.txt")
    session = PromptSession(history=history)
    
    
    while True:
        try:
            user_input = session.prompt('RedFrizzi> ')
            
            if user_input=="exit":
                cprint("BYE BYE!!","red")
                break

            if  user_input=="":
                continue

            if not user_input.startswith("rf") or user_input=="rf":
                cprint("Enter \"rf -h\" to see the options",'yellow')
                continue

            if "rf --clear" in user_input and len(user_input.strip().split(" "))== 2:
                clear()

            if "rf --init" in user_input:
                init()
                load_dotenv("env")

            if "rf -h" in user_input and len(user_input.strip().split(" "))==2:
                cprint("""
                Usage: [rf -options]
                -t <target> : Enter the target name
                -f < input_filename> : Load target names from file
                -o <output_filname> : Print response to <output_file>
                --john <inputfile>: Create outputfile for John using <inputfile>
                --init : Set API Key
                --clear : Reset terminal
                
                ""","yellow")
                
                
            if "rf -t " in user_input and  len(user_input.strip().split(" ")) in [3,5]:
                target=user_input.split(" ")[2].strip()
                base_querystring["term"]= target
                res= do_get(url,headers,base_querystring)
                print("TARGET: " + target.upper())
                if "-o " in user_input:
                    output_file=user_input.split(" ")[4].strip()
                    with open(output_file,"a") as of:
                        of.write('{ "records": [')
                        #of.write(target.upper())
                        res_asjson=dict()
                        res_asjson["name"]= target.upper()
                        res_asjson.update(json.loads(res))
                        of.write(json.dumps(res_asjson,indent=4))
                        of.write(']}')
                else:
                    print(res)
            
            if "rf --john" in user_input and len(user_input.strip().split(" "))==3:

                input_file= user_input.split(" ")[2].strip()
                output_file= input_file + ".john"
                jp=JohnParser(inputfile=input_file,outputfile=output_file)
                jp.create_johnfile()



            if "rf -f " in user_input and  len(user_input.strip().split(" ")) in [3,5]:
                input_file=user_input.split(" ")[2].strip()
                
                with open(input_file,"r")  as ipf:
                    if "-o " in user_input:
                        output_file=user_input.split(" ")[4].strip()
                        with open(output_file,"a") as of:
                            of.write('{ "records": [')
                            line1,line2 = ipf.readline(),ipf.readline()
                            while True:
                                line1=line1.strip()
                                base_querystring["term"]= line1
                                print("CURRENT TARGET: " +line1.upper())
                                res1= do_get(url,headers,base_querystring)
                                time.sleep(1.2)
                                #res1_asjson=dict()
                                #res1_asjson["name"]= line1.upper()
                                #res1_asjson.update(json.loads(res1))
                                #of.write(json.dumps(res1_asjson,indent=4))
                                write_res_query(target=line1,outputfile=of,result_query=res1)
                                line2=line2.strip()
                                base_querystring["term"]= line2
                                print("CURRENT TARGET: " +line2.upper())
                                res2= do_get(url,headers,base_querystring)
                                time.sleep(1.2)
                                of.write(",")
                                #res2_asjson=dict()
                                #res2_asjson["name"]= line2.upper()
                                #res2_asjson.update(json.loads(res2))
                                #of.write(json.dumps(res2_asjson,indent=4))
                                write_res_query(target=line2,outputfile=of,result_query=res2)
                                line1,line2 = ipf.readline(),ipf.readline()
                                line1=line1.strip()
                                line2=line2.strip()
                                if not line1 and not line2: # even
                                    break
                                of.write(",")
                                if line1 and not line2: # odd
                                    base_querystring["term"]= line1
                                    print("CURRENT TARGET: " +line1.upper())
                                    res1= do_get(url,headers,base_querystring)
                                    time.sleep(1.2)
                                    write_res_query(target=line1,outputfile=of,result_query=res1)
                                    break
                                   
                            of.write(']}')
                            

                    else:
                        for line in ipf:
                                line=line.strip()
                                base_querystring["term"]= line
                                print(line)
                                res= do_get(url,headers,base_querystring)
                                print("CURRENT TARGET: " +line.upper())
                                print(res)
                                time.sleep(1.2)
        except KeyboardInterrupt:
            cprint("BYE BYE!!",'red')
            break
            

if __name__=="__main__":
    
    main()
