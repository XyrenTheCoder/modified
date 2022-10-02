import os, time, pickle, requests

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
    else: return dict()

def save(uname, dat):
    data = load_data()
    data[uname] = dat
    with open(fn, "wb") as file: pickle.dump(data, file)
        
def load(uname):
    data = load_data()
    if uname not in data: return Data(0, 0, 0)
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

def recur_func():
    try:
        e = load("1")
        msg = input(f"{e.username}: ")
        if len(msg) == 0 or msg == " ": print("[system] You cannot send empty messages.")
        elif len(msg) > 2000: 
            overlen = len(msg) - 2000
            print(f"[system] Your message is {overlen} characters longer than the length limit, please shorten it and try again.")
        else: send(msg)
    except: pass
    finally: return recur_func()

#when run
e = load("1")
clear()
print(f"[system] You have joined the chat as {e.username}.")
while True: recur_func()
