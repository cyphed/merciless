import os
import base64
import pyfiglet
import colorama
# Update Function
import urllib.request
webUrl  = urllib.request.urlopen('https://pastebin.com/raw/kMd4aDqA')
data = webUrl.read()
if('no' in data.decode()):
  print('Thanks for using Merciless.')

else:
   print('Merciless needs updating, please reclone the product.')
   exit()
# Loading Screen & Menu
print(colorama.Fore.GREEN+"Installing Requirements...")
done = False
os.system(f"python3 -m pip install psutil colorama pyfiglet pywget logging uuid")
done = True
if os.name=="nt":
    os.system("cls")
else:
    os.system("clear")
print(colorama.Fore.BLUE+"""

   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
    |     |     |     |     |     |     |     |     |     |     |     |     | 
90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
    |           . _..::__:  ,-"-"._        |7       ,     _,.__             |
    |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
    |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|
60N-+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +-60N
    | '"'     \         "    _L        oD_,--'                )     /. (|   |
    |          |           ,'          _)_.\\._<> 6              _,' /  '    |
    |          `.         /           [_/_'` `"(                <'}  )      |
30N-+           \\    .-. )           /   `-'"..' `:._          _)  '        +-30N
    |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
    |              `._,   ""         |           \`'   \|   ?_)  {\         |
    |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
000-+                   |    `-._         |     /          `:`<_|h--._      +-000
    |                   (        >        .     | ,          `=.__.`-'\     |
    |                    `.     /         |     |{|              ,-.,\     .|
    |   >~Merciless~<     |   ,'           \   / `'            ,"     \     |
30S-+     >~V.7.0~<       |  /              |_'                |  __  /     +-30S
    |                     | |                                  '-'  `-'   \.|
    |                     |/                                         "    / |
    |                     \.                                             '  |
60S-+                                                                       +-60S
    |                      ,/            ______._.--._ _..---.---------._   |
    |     ,-----"-..?----_/ )      __,-'"             "                  (  |
    |-.._(                  `-----'                                       `-|
90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S
    |     |     |     |     |     |     |     |     |     |     |     |     |
   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
-----------------------------------------------------------------------------
[1] - Select a icon for your .EXE Virus      [2] - Create The EXE
[3] - Support Server                         [4] - Exit
""")
# Malware creation function
def main():
    inp = input("[<merciless@meli>] - ")
    if inp == "1" or inp == "icon":
        print("[<merciless@meli>] - Please make sure the file is called img and the file type .png ")
    if inp == "2" or inp == "create":
        os.system("pyinstaller --onefile --icon=img.png virus/merciless.py")
    if inp == "3" or inp == "support":
        print("merciless | https://discord.gg/meli")
    if inp == "4" or inp == "exit":
       exit()
    else:
        main()
main()

