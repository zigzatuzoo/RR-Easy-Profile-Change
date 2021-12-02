import requests
import recnetlogin as rnl
import urllib
import time
import os


'''STUFF YOU WANT TO CHANGE'''
USER = ''
PASS = ''
'''Bio slots'''
BioSlot1 = '''Example bio'''

BioSlot2 = '''bio
example'''

BioSlot3 = '''Bio                      Example'''

BioSlot4 = '''I am a Funny man'''

BioSlot5 = '''Code'''

BioSlot6 = '''https://Github.com/zigzatuzoo/RR-Easy-Profile-Change
Have fun!'''

'''PFP slots'''
PFPSlot1 = '8d6ec536fd6c4b0a916da855aa6b879b.jpg'

PFPSlot2 = '6bb5a2b0e9ba4743b977af117772f4f5.jpg'

PFPSlot3 = 'f36cec6068994c1180ecbd554b279ada.jpg'

PFPSlot4 = '355c2c7e87f0489bb5f0308cdec108f6.jpg'

PFPSlot5 = '49b2788b672e4088a25eb0a9eff35c17.jpg'

PFPSlot6 = '2d83af05944d49c69fa9565fb238a91b.jpg'

'''INIT VARS'''
ah = {}

def clear():
    if os.name == 'nt' or os.name == 'dos':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

'copy this for stuff "ah = log()"'

def log():
    token = rnl.login_to_recnet(USER, PASS).access_token
    authheader = {'Authorization':token}
    return authheader

def changeBio(submitBio):
    ah = log()
    parsedbio = urllib.parse.quote(submitBio)
    print(parsedbio)
    bioUrl = 'https://accounts.rec.net/account/me/bio'
    requests.put(bioUrl, headers=ah, data=parsedbio)
    print('Bio successfully changed, set to\n'+'URLEncode:'+parsedbio+'\nNon URLEncode:\n'+submitBio)
    print('Done, Back to main menu')
    mainMenu()

def changePFP(imageURL):
    ah = log()
    requests.put('https://accounts.rec.net/account/me/profileImage', headers = ah, data = imageURL)
    print('Successfully changed the profile picture')
    print('Going back to main menu')
    mainMenu()


def Startup():
    print('''
 __      __       .__                                ._.                                     
/  \    /  \ ____ |  |   ____  ____   _____   ____   | |                                       
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  | |                                       
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   \|                                       
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  __                                       
       \/       \/          \/            \/     \/   \/                                       
__________                                ___________ _______________________________________  
\______   \_______   ____   ______ ______ \_   _____/ \      \__    ___/\_   _____/\______   \ 
 |     ___/\_  __ \_/ __ \ /  ___//  ___/  |    __)_  /   |   \|    |    |    __)_  |       _/ 
 |    |     |  | \/\  ___/ \___ \ \___ \   |        \/    |    \    |    |        \ |    |   \ 
 |____|     |__|    \___  >____  >____  > /_______  /\____|__  /____|   /_______  / |____|_  / 
                        \/     \/     \/          \/         \/                 \/         \/  
  __                                __  .__                                                    
_/  |_  ____     ____  ____   _____/  |_|__| ____  __ __   ____                                
\   __\/  _ \  _/ ___\/  _ \ /    \   __\  |/    \|  |  \_/ __ \                               
 |  | (  <_> ) \  \__(  <_> )   |  \  | |  |   |  \  |  /\  ___/                               
 |__|  \____/   \___  >____/|___|  /__| |__|___|  /____/  \___  >                              
                    \/           \/             \/            \/    ''')
    input()
    
    if USER == '':
        print('No username specified, add the login information in line 9 and 10 of the script')
        exit()
    if PASS == '':
        print('No password specified, add the login information in line 9 and 10 of the script')
        exit()
    ah = log()
    testLogin = requests.get('https://accounts.rec.net/account/me',headers=ah)
    
    if testLogin.status_code == 401:
        print('Login error, please check account details.')
    elif testLogin.status_code == 200:
        print('Login success, going to main menu.')
    else:
        print('Unknown login error, cannot continue. Exiting.')
        exit()
    time.sleep(3)
    
    mainMenu()

def mainMenu():
    clear()
    print('''Use numbers for the following
    1 to go to the change bio menu
    2 to go to the change pfp menu
    exit to exit''')
    menuresponce = input()

    if menuresponce == '1':
        menuresponce = ''
        bioMenu()
    elif menuresponce == '2':
        menuresponce = ''
        pfpMenu()
    elif menuresponce == 'exit':
        print('Exiting.')
        exit()
    else:
        print('{} is not one of the options'.format(menuresponce))

def bioMenu():
    clear()
    print('''
    What saved Bio's do you want to use?
    1 - {}
    2 - {}
    3 - {}
    4 - {}
    5 - {}
    6 - {}
    exit - go back to main menu
    
    Keep in mind these can be changed via the BioSlot variables at the beginning of the script'''.format(BioSlot1,BioSlot2,BioSlot3,BioSlot4,BioSlot5,BioSlot6))
    ures = input()
    if ures == '1':
        changeBio(BioSlot1)
    elif ures == '2':
        changeBio(BioSlot2)
    elif ures == '3':
        changeBio(BioSlot3)
    elif ures == '4':
        changeBio(BioSlot4)
    elif ures == '5':
        changeBio(BioSlot5)
    elif ures == '6':
        changeBio(BioSlot6)
    elif ures == 'exit':
        mainMenu()
    elif ures == '':
        print("You didn't input anything.")
        time.sleep(1)
        bioMenu()
    else:
        print('{} is not an accepted responce.'.format(ures))
        bioMenu()

def pfpMenu():
    clear()
    print('''
    What saved PFP's do you want to use?
    1 - {}
    2 - {}
    3 - {}
    4 - {}
    5 - {}
    6 - {}
    exit - go back to main menu
    
    Keep in mind these can be changed via the PFPSlot variables at the beginning of the script'''.format(PFPSlot1,PFPSlot2,PFPSlot3,PFPSlot4,PFPSlot5,PFPSlot6))

    ures = input()
    if ures == '1':
        changePFP(PFPSlot1)
    elif ures == '2':
        changePFP(PFPSlot2)
    elif ures == '3':
        changePFP(PFPSlot3)
    elif ures == '4':
        changePFP(PFPSlot4)
    elif ures == '5':
        changePFP(PFPSlot5)
    elif ures == '6':
        changePFP(PFPSlot6)
    elif ures == 'exit':
        mainMenu()
    elif ures == '':
        print("You didn't input anything.")
        time.sleep(1)
        pfpMenu()
    else:
        print('{} is not an accepted responce.'.format(ures))
        pfpMenu()

Startup()
