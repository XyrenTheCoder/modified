#WARNING: a file named ".data" will appear in the same directory, DO NOT DELETE
# me fixed grammar and details xd - archisha at 16:04
import os
import time
import pickle
import requests
from threading import Thread
from getpass import getpass

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

def fetchmsg():
    oldmsg = ''
    while True:
        r = requests.get("https://rqchat.thatonearchuser.repl.co/getlatest")
        if r.status_code == 200:
            if r.text == oldmsg or len(r.text) == 0: pass 
            else: print(r.text)
        else: print(f"{r.text}, return status: {r.status_code}")
        oldmsg = r.text
        time.sleep(0.5)

def fetchall():
    r = requests.get("https://rqchat.thatonearchuser.repl.co/fetchall")
    if r.status_code == 200: print(r.text)
    else: print(f"{r.text}, return status: {r.status_code}")

def register(name, passwd):
    if " " in name: return "Your username cannot contain spaces"
    if " " in passwd: return "Your password cannot contain spaces"
    r = requests.get(f"https://rqchat.thatonearchuser.repl.co/register?username={name}&password={passwd}")
    if r.status_code == 200:
        d = load("1")
        d.username = name
        d.clientid = r.text
        save("1", d)
        print("Successfully registered!")
    else: 
        print(f"{r.text}, return status: {r.status_code}")
        input()
        exit(1)

def login(name, passwd):
    r = requests.get(f"https://rqchat.thatonearchuser.repl.co/login?username={name}&password={passwd}")
    if r.status_code == 200: return r.text
    else:
        print(r.text)
        return False

def clear():
    if os.name == 'nt': os.system("cls")
    else: os.system("clear")

def init():
    d = load("1")
    while True:
        try:
            inp = int(input("Options:\n1. Login\n2. Register\nType your option:"))
            if int(inp) == 1 or int(inp) == 2: break
        except ValueError: print("Invalid value")
        clear()
    if inp == 1:
        while True:
            clear()
            if d.username != 0:
                print(f"Hi, {d.username}! To login, please insert your password")
                usr = d.username
            elif d.username == 0:
                usr = input("Username: ")
            passwrd = getpass("Password: ")
            var = login(usr, passwrd)
            d.username = usr
            d.clientid = var
            save("1", d)
            if var != False: break
            else: print(var)
            input("press enter to continue")
    elif inp == 2:
        uname = input(f"Username: ")
        while True:
            clear()
            passw = getpass("Password: ")
            passconf = getpass("Confirm password: ")
            if passw == passconf: break
            else: print("Password does not match")
            input("press enter to continue")
        register(uname, passconf)
    d.running = "true"
    save("1", d)
    #global thread1
    #thread1 = Thread(target=fetchmsg)
    #thread1.start()
    fetchmsg()
    print("Start inputHandler2.py to send messages\n")

try: init()
except KeyboardInterrupt:
    print("Cleaning up...")
    thread1.stop()
    d = load("1")
    d.running = "false"
    save("1", d)
    exit(0)