import requests
import recnetlogin as rnl
import urllib

USER = ''
PASS = ''

'''STUFF YOU WANT TO CHANGE'''
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
PFPSlot1 = 'https://img.rec.net/8d6ec536fd6c4b0a916da855aa6b879b.jpg'

PFPSlot2 = 'https://img.rec.net/6bb5a2b0e9ba4743b977af117772f4f5.jpg'

PFPSlot3 = 'https://img.rec.net/f36cec6068994c1180ecbd554b279ada.jpg'

PFPSlot4 = 'https://img.rec.net/355c2c7e87f0489bb5f0308cdec108f6.jpg'

PFPSlot5 = 'https://img.rec.net/49b2788b672e4088a25eb0a9eff35c17.jpg'

PFPSlot6 = 'https://img.rec.net/2d83af05944d49c69fa9565fb238a91b.jpg'

'''INIT VARS'''
ah = {}


'copy this for stuff "ah = log()"'

def log():
    token = rnl.login_to_recnet(USER, PASS).access_token
    authheader = {'Authorization':token}
    return authheader

def changeBio(submitBio):
    parsedbio = urllib.parse.quote(submitBio)
    print(parsedbio)
    bioUrl = 'https://accounts.rec.net/account/me/bio'
    requests.put(bioUrl, headers=ah, data=parsedbio)
    print('Bio successfully changed, set to\n'+'URLEncode:'+parsedbio+'\nNon URLEncode:\n'+submitBio)
    print('Done, Back to main menu')

def changePFP(imageURL):
    imageURL=1


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
    mainMenu()

def mainMenu():
    print('''Use numbers for the following
    1 to go to the change bio menu
    2 to go to the change pfp menu''')
    menuresponce = input()

    if menuresponce == 1:
        menuresponce = ''
        bioMenu()
    elif menuresponce == 2:
        menuresponce = ''
        pfpMenu()
    else:
        print('{} is not one of the options'.format(menuresponce))

def bioMenu():
    print('')

def pfpMenu():
    print('')

Startup()