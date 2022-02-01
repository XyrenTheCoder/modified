import os
import requests
import pickle
import time

fn = f"{os.getcwd()}/.data"

class Data:
    def __init__(self, username, clientid, running):
        self.username = username
        self.clientid = clientid
        self.running = running

def load_data():
    if os.path.isfile(fn):
        with open(fn, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def save(uname, dat):
    data = load_data()
    data[uname] = dat
    with open(fn, "wb") as file:
        pickle.dump(data, file)
        
def load(uname):
    data = load_data()
    if uname not in data:
        return Data(0, 0, 0)
    return data[uname]

def checkrun() -> bool:
    d = load("1")
    if d.username == 0: return False
    if d.running == "true": return True
    elif d.running == "false": return False

def send(msg):
    d = load("1")
    r = requests.get(f"https://rqchat.thatonearchuser.repl.co/send?username={d.username}&msg={msg}&cid={d.clientid}")
    if r.status_code == 200: return True
    else: print(r.text)

def clear():
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")
    
#if checkrun(): pass
#else: raise SystemExit("messageHandler is not running")

#when 
print(f"[system] You have joined the chat successfully.\nWelcome to the beta version of Rqchat (idk what name to put here lol)! \nType ]info to get more info.\n")
time.sleep(5)
x = input("- press enter to dismiss this message or type \" ]info \" to get information -\n> ")

if x == "]info": 
    clear()
    print("[info] This is an modified inputHandler for the modified messageHandler by αrchιshα#5518 (discord). Rqchat is a simple chatroom system written in Python. The original author is thatOneArchUser#5794 (discord).\nYou can chat here freely by simply typing messages in the \" >>> \" and send them by pressing enter.\nYou cannot send an empty message or simply send some spaces.\nThe maximum character length limit is 2000.\nWe hope you can have a enjoyable experience here!\n(This is a beta version, you may come across few bugs. Feel free to report them by DMing us in Discord!)\n")
    input("- press enter to dismiss -\n> ")

while True:
    clear()
    print("level: modified medium\n[WARNING] You are currently using a modified version of inputHandler!\n")
    msg = input(">>> ")
    if len(msg) == 0 or msg == " ":
        print("[failed] You cannot send empty messages")
        time.sleep(2)
    elif len(msg) > 2000: 
        overlen = len(msg) - 2000
        print(f"[failed] Your message is {overlen} characters longer than the length limit, please shorten it and try again")
        time.sleep(2)
    else: 
        send(msg)



#btw i use ____
