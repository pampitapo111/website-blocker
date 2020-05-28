import time
from playsound import playsound


websites = [] #websites to be blocked#
ip = '127.0.0.1'

while True:
    web = input('Enter a website you want to block. Type done to exit. ')
    if web == 'done':
        break
    websites.append(web)

t = int(input('How long would you want to block these websites? (in seconds)'))
f = open("c:\\windows\\system32\\drivers\\etc\\hosts","r+")
for i in range(len(websites)):
    list = (ip+ ' '+websites[i] + '\n')
    f.write(list)
f.close()

while t:
    
    time.sleep(1)
    t -= 1
    print("NOT ALLOWED")
    
f = open("directory\\of\\your\\file","w")
f.write(" ")
f.close()
playsound('directory\\of\\your\\file.mp3')
print(":)")
