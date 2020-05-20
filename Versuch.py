#!/usr/bin/env python

import pygame, sys

import datetime

import numpy as np

#Versuch email:

import imaplib
import email

username = 'adampythonmirror@gmail.com'
password = 'Herbt12345'

#mail = imaplib.IMAP4_SSL("imap.gmail.com")
#mail.login(username,password)

#mail.select("inbox")

#result, data = mail.uid('search',None, "ALL")

#inbox_item_list = data[0].split()

#most_recent = inbox_item_list[-1]

#oldest = inbox_item_list[0]

#result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')

#raw_email = email_data[0][1]#.decode("utf-8")

#email_message = email.message_from_string(raw_email)

#email_message['From']
#email_message['Subject']


mess2Val1 = 0;
mess2Val2 = 0;
mess2Val3 = 0;
mess2Val3 = 0;
mess2Val4 = 0;
mess2Val5 = 0;
mess2Val6 = 0;
mess2Val7 = 0;
mess2Val8 = 0;
mess2Val9 = 0;
mess2Val10 = 0;
mess2Val11 = 0;
mess2Val12 = 0;
mess2Val13 = 0;
mess2Val14 = 0;
mess2Val15 = 0;
mess2Val16 = 0;
mess2Val17 = 0;
mess2Val18 = 0;
mess2Val19 = 0;
mess2Val20 = 0;
mess2Val21 = 0;
mess2Val22 = 0;
mess2Val23 = 0;
mess2Val24 = 0;
mess2Val25 = 0;
mess2Val26 = 0;
mess2Val27 = 0;
mess2Val28 = 0;
mess2Val29 = 0;
mess2Val30 = 0;
mess2Val31 = 0;
mess2Val32 = 0;
mess2Val33 = 0;
mess2Val34 = 0;
mess2Val35 = 0;
mess2Val36 = 0;
mess2Val37 = 0;
mess2Val38 = 0;
mess2Val39 = 0;
mess2Val40 = 0;
mess2Val41 = 0;
mess2Val42 = 0;
mess2Val43 = 0;
mess2Val44 = 0;
mess2Val45 = 0;
mess2Val46 = 0;
mess2Val47 = 0;
mess2Val48 = 0;
mess2Val49 = 0;
mess2Val50 = 0;
mess2Val51 = 0;
mess2Val52 = 0;
mess2Val53 = 0;




from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000, 1000), 0, 32)

backgroundfile = "background.png"
mousefile = "mouse.png"

background = pygame.image.load(backgroundfile).convert()
mouse = pygame.image.load(mousefile).convert_alpha()

#scoreValue = 'hallo'

#message1Value = email_message['From']
#message2Value = email_message['Subject']

kuerzSubject = range(53)
mess2Val = range(53)
isTrue = range(53)
messSend = []
#list1 = [1, 20, 3]

minVal = '00'
    
font = pygame.font.Font('Roboto-Light.ttf',32)
    
textX = 5
textY = 5
    
def show_messages(x,y):
    message = font.render("From : " + mess1Val, True, (255,255,255))
    screen.blit(message, (x, y+100))
    message2 = font.render("Subject : " + message2Value, True, (255,255,255))
    screen.blit(message2, (x, y+150))
    
def show_datetime(x,y):
    hour = font.render(str(hourValue), True, (255,255,255))
    screen.blit(hour, (x+380, y))
    minute = font.render(" : " + minVal, True, (255,255,255))
    screen.blit(minute, (x+410, y))

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    for i in range(0, 52):
        kuerzSubject[i] = 0
        mess2Val[i] = 0
        isTrue[i] = 0
        #messSend[i] = 0
    
    
    #init done, now main part
    
    screen.blit(background, (0,0))
    #screen.fill((0,0,0))
    #pygame.display.update()
    
    x,y = pygame.mouse.get_pos()
    
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2
    
    screen.blit(mouse, (x,y))
    
    #mein Versuch Text:
    
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username,password)

    mail.select("inbox")

    result, data = mail.uid('search',None, "ALL")

    inbox_item_list = data[0].split()

    most_recent = inbox_item_list[-1]

    oldest = inbox_item_list[0]

    result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')

    raw_email = email_data[0][1]#.decode("utf-8")

    email_message = email.message_from_string(raw_email)
    
    message1Value = email_message['From']
    #TRY:
    kuerzFrom1 = message1Value.find('<')+1
    kuerzFrom2 = message1Value.find('>')
    mess1Val = message1Value[kuerzFrom1:kuerzFrom2]
    
    message2Value = email_message['Subject']
    #TRY Behinderter Algorythmus:
    if message2Value.find('0A') != -1:
        kuerzSubject[0] = message2Value.find('0A')+1
        kuerzSubject1 = message2Value.find('=', kuerzSubject[0], kuerzSubject[0]+30)
        mess2Val[0] = message2Value[kuerzSubject[0]:kuerzSubject1]
        isTrue[0] = 1
    if message2Value.find('0B') != -1:
        kuerzSubject[1] = message2Value.find('0B')+1
        kuerzSubject2 = message2Value.find('=', kuerzSubject[1], kuerzSubject[1]+30)
        mess2Val[1] = message2Value[kuerzSubject[1]:kuerzSubject2]
        isTrue[1] = 1
    if message2Value.find('0C') != -1:
        kuerzSubject[2] = message2Value.find('0C')+1
        kuerzSubject3 = message2Value.find('=', kuerzSubject[2], kuerzSubject[2]+30)
        mess2Val[2] = message2Value[kuerzSubject[2]:kuerzSubject3]
        isTrue[2] = 1
    if message2Value.find('0D') != -1:
        kuerzSubject[3] = message2Value.find('0D')+1
        kuerzSubject4 = message2Value.find('=', kuerzSubject[3], kuerzSubject[3]+30)
        mess2Val[3] = message2Value[kuerzSubject[3]:kuerzSubject4]
        isTrue[3] = 1
    if message2Value.find('0E') != -1:
        kuerzSubject[4] = message2Value.find('0E')+1
        kuerzSubject5 = message2Value.find('=', kuerzSubject[4], kuerzSubject[4]+30)
        mess2Val[4] = message2Value[kuerzSubject[4]:kuerzSubject5]
        isTrue[4] = 1
    if message2Value.find('0F') != -1:
        kuerzSubject[5] = message2Value.find('0F')+1
        kuerzSubject6 = message2Value.find('=', kuerzSubject[5], kuerzSubject[5]+30)
        mess2Val[5] = message2Value[kuerzSubject[5]:kuerzSubject6]
        isTrue[5] = 1
    if message2Value.find('0G') != -1:
        kuerzSubject[6] = message2Value.find('0G')+1
        kuerzSubject7 = message2Value.find('=', kuerzSubject[6], kuerzSubject[6]+30)
        mess2Val[6] = message2Value[kuerzSubject[6]:kuerzSubject7]
        isTrue[6] = 1
    if message2Value.find('0H') != -1:
        kuerzSubject[7] = message2Value.find('0H')+1
        kuerzSubject8 = message2Value.find('=', kuerzSubject[7], kuerzSubject[7]+30)
        mess2Val[7] = message2Value[kuerzSubject[7]:kuerzSubject8]
        isTrue[7] = 1
    if message2Value.find('0I') != -1:
        kuerzSubject[8] = message2Value.find('0I')+1
        kuerzSubject9 = message2Value.find('=', kuerzSubject[8], kuerzSubject[8]+30)
        mess2Val[8] = message2Value[kuerzSubject[8]:kuerzSubject9]
        isTrue[8] = 1
    if message2Value.find('0J') != -1:
        kuerzSubject[9] = message2Value.find('0J')+1
        kuerzSubject10 = message2Value.find('=', kuerzSubject[9], kuerzSubject[9]+30)
        mess2Val[9] = message2Value[kuerzSubject[9]:kuerzSubject10]
        isTrue[9] = 1
    if message2Value.find('0K') != -1:
        kuerzSubject[10] = message2Value.find('0K')+1
        kuerzSubject11 = message2Value.find('=', kuerzSubject[10], kuerzSubject[10]+30)
        mess2Val[10] = message2Value[kuerzSubject[10]:kuerzSubject11]
        isTrue[10] = 1
    if message2Value.find('0L') != -1:
        kuerzSubject[11] = message2Value.find('0L')+1
        kuerzSubject12 = message2Value.find('=', kuerzSubject[11], kuerzSubject[11]+30)
        mess2Val[11] = message2Value[kuerzSubject[11]:kuerzSubject12]
        isTrue[11] = 1
    if message2Value.find('0M') != -1:
        kuerzSubject[12] = message2Value.find('0M')+1
        kuerzSubject13 = message2Value.find('=', kuerzSubject[12], kuerzSubject[12]+30)
        mess2Val[12] = message2Value[kuerzSubject[12]:kuerzSubject13]
        isTrue[12] = 1
    if message2Value.find('0N') != -1:
        kuerzSubject[13] = message2Value.find('0N')+1
        kuerzSubject14 = message2Value.find('=', kuerzSubject[13], kuerzSubject[13]+30)
        mess2Val[13] = message2Value[kuerzSubject[13]:kuerzSubject14]
        isTrue[13] = 1
    if message2Value.find('0O') != -1:
        kuerzSubject[14] = message2Value.find('0O')+1
        kuerzSubject15 = message2Value.find('=', kuerzSubject[14], kuerzSubject[14]+30)
        mess2Val[14] = message2Value[kuerzSubject[14]:kuerzSubject15]
        isTrue[14] = 1
    if message2Value.find('0P') != -1:
        kuerzSubject[15] = message2Value.find('0P')+1
        kuerzSubject16 = message2Value.find('=', kuerzSubject[15], kuerzSubject[15]+30)
        mess2Val[15] = message2Value[kuerzSubject[15]:kuerzSubject16]
        isTrue[15] = 1
    if message2Value.find('0Q') != -1:
        kuerzSubject[16] = message2Value.find('0Q')+1
        kuerzSubject17 = message2Value.find('=', kuerzSubject[16], kuerzSubject[16]+30)
        mess2Val[16] = message2Value[kuerzSubject[16]:kuerzSubject17]
        isTrue[16] = 1
    if message2Value.find('0R') != -1:
        kuerzSubject[17] = message2Value.find('0R')+1
        kuerzSubject18 = message2Value.find('=', kuerzSubject[17], kuerzSubject[17]+30)
        mess2Val[17] = message2Value[kuerzSubject[17]:kuerzSubject18]
        isTrue[17] = 1
    if message2Value.find('0S') != -1:
        kuerzSubject[18] = message2Value.find('0S')+1
        kuerzSubject19 = message2Value.find('=', kuerzSubject[18], kuerzSubject[18]+30)
        mess2Val[18] = message2Value[kuerzSubject[18]:kuerzSubject19]
        isTrue[18] = 1
    if message2Value.find('0T') != -1:
        kuerzSubject[19] = message2Value.find('0T')+1
        kuerzSubject20 = message2Value.find('=', kuerzSubject[19], kuerzSubject[19]+30)
        mess2Val[19] = message2Value[kuerzSubject[19]:kuerzSubject20]
        isTrue[19] = 1
    if message2Value.find('0U') != -1:
        kuerzSubject[20] = message2Value.find('0U')+1
        kuerzSubject21 = message2Value.find('=', kuerzSubject[20], kuerzSubject[20]+30)
        mess2Val[20] = message2Value[kuerzSubject[20]:kuerzSubject21]
        isTrue[20] = 1
    if message2Value.find('0V') != -1:
        kuerzSubject[21] = message2Value.find('0V')+1
        kuerzSubject22 = message2Value.find('=', kuerzSubject[21], kuerzSubject[21]+30)
        mess2Val[21] = message2Value[kuerzSubject[21]:kuerzSubject22]
        isTrue[21] = 1
    if message2Value.find('0W') != -1:
        kuerzSubject[22] = message2Value.find('0W')+1
        kuerzSubject23 = message2Value.find('=', kuerzSubject[22], kuerzSubject[22]+30)
        mess2Val[22] = message2Value[kuerzSubject[22]:kuerzSubject23]
        isTrue[22] = 1
    if message2Value.find('0X') != -1:
        kuerzSubject[23] = message2Value.find('0X')+1
        kuerzSubject24 = message2Value.find('=', kuerzSubject[23], kuerzSubject[23]+30)
        mess2Val[23] = message2Value[kuerzSubject[23]:kuerzSubject24]
        isTrue[23] = 1
    if message2Value.find('0Y') != -1:
        kuerzSubject[24] = message2Value.find('0Y')+1
        kuerzSubject25 = message2Value.find('=', kuerzSubject[24], kuerzSubject[24]+30)
        mess2Val[24] = message2Value[kuerzSubject[24]:kuerzSubject25]
        isTrue[24] = 1
    if message2Value.find('0Z') != -1:
        kuerzSubject[25] = message2Value.find('0Z')+1
        kuerzSubject26 = message2Value.find('=', kuerzSubject[25], kuerzSubject[25]+30)
        mess2Val[25] = message2Value[kuerzSubject[25]:kuerzSubject26]
        isTrue[25] = 1
    if message2Value.find('0a') != -1:
        kuerzSubject[26] = message2Value.find('0a')+1
        kuerzSubject27 = message2Value.find('=', kuerzSubject[26], kuerzSubject[26]+30)
        mess2Val[26] = message2Value[kuerzSubject[26]:kuerzSubject27]
        isTrue[26] = 1
    if message2Value.find('0b') != -1:
        kuerzSubject[27] = message2Value.find('0b')+1
        kuerzSubject28 = message2Value.find('=', kuerzSubject[27], kuerzSubject[27]+30)
        mess2Val[27] = message2Value[kuerzSubject[27]:kuerzSubject28]
        isTrue[27] = 1
    if message2Value.find('0c') != -1:
        kuerzSubject[28] = message2Value.find('0c')+1
        kuerzSubject29 = message2Value.find('=', kuerzSubject[28], kuerzSubject[28]+30)
        mess2Val[28] = message2Value[kuerzSubject[28]:kuerzSubject29]
        isTrue[28] = 1
    if message2Value.find('0d') != -1:
        kuerzSubject[29] = message2Value.find('0d')+1
        kuerzSubject30 = message2Value.find('=', kuerzSubject[29], kuerzSubject[29]+30)
        mess2Val[29] = message2Value[kuerzSubject[29]:kuerzSubject30]
        isTrue[29] = 1
    if message2Value.find('0e') != -1:
        kuerzSubject[30] = message2Value.find('0e')+1
        kuerzSubject31 = message2Value.find('=', kuerzSubject[30], kuerzSubject[30]+30)
        mess2Val[30] = message2Value[kuerzSubject[30]:kuerzSubject31]
        isTrue[30] = 1
    if message2Value.find('0f') != -1:
        kuerzSubject[31] = message2Value.find('0f')+1
        kuerzSubject32 = message2Value.find('=', kuerzSubject[31], kuerzSubject[31]+30)
        mess2Val[31] = message2Value[kuerzSubject[31]:kuerzSubject32]
        isTrue[31] = 1
    if message2Value.find('0g') != -1:
        kuerzSubject[32] = message2Value.find('0g')+1
        kuerzSubject33 = message2Value.find('=', kuerzSubject[32], kuerzSubject[32]+30)
        mess2Val[32] = message2Value[kuerzSubject[32]:kuerzSubject33]
        isTrue[32] = 1
    if message2Value.find('0h') != -1:
        kuerzSubject[33] = message2Value.find('0h')+1
        kuerzSubject34 = message2Value.find('=', kuerzSubject[33], kuerzSubject[33]+30)
        mess2Val[33] = message2Value[kuerzSubject[33]:kuerzSubject34]
        isTrue[33] = 1
    if message2Value.find('0i') != -1:
        kuerzSubject[34] = message2Value.find('0i')+1
        kuerzSubject35 = message2Value.find('=', kuerzSubject[34], kuerzSubject[34]+30)
        mess2Val[34] = message2Value[kuerzSubject[34]:kuerzSubject35]
        isTrue[34] = 1
    if message2Value.find('0j') != -1:
        kuerzSubject[35] = message2Value.find('0j')+1
        kuerzSubject36 = message2Value.find('=', kuerzSubject[35], kuerzSubject[35]+30)
        mess2Val[35] = message2Value[kuerzSubject[35]:kuerzSubject36]
        isTrue[35] = 1
    if message2Value.find('0k') != -1:
        kuerzSubject[36] = message2Value.find('0k')+1
        kuerzSubject37 = message2Value.find('=', kuerzSubject[36], kuerzSubject[36]+30)
        mess2Val[36] = message2Value[kuerzSubject[36]:kuerzSubject37]
        isTrue[36] = 1
    if message2Value.find('0l') != -1:
        kuerzSubject[37] = message2Value.find('0l')+1
        kuerzSubject38 = message2Value.find('=', kuerzSubject[37], kuerzSubject[37]+30)
        mess2Val[37] = message2Value[kuerzSubject[37]:kuerzSubject38]
        isTrue[37] = 1
    if message2Value.find('0m') != -1:
        kuerzSubject[38] = message2Value.find('0m')+1
        kuerzSubject39 = message2Value.find('=', kuerzSubject[38], kuerzSubject[38]+30)
        mess2Val[38] = message2Value[kuerzSubject[38]:kuerzSubject39]
        isTrue[38] = 1
    if message2Value.find('0n') != -1:
        kuerzSubject[39] = message2Value.find('0n')+1
        kuerzSubject40 = message2Value.find('=', kuerzSubject[39], kuerzSubject[39]+30)
        mess2Val[39] = message2Value[kuerzSubject[39]:kuerzSubject40]
        isTrue[39] = 1
    if message2Value.find('0o') != -1:
        kuerzSubject[40] = message2Value.find('0o')+1
        kuerzSubject41 = message2Value.find('=', kuerzSubject[40], kuerzSubject[40]+30)
        mess2Val[40] = message2Value[kuerzSubject[40]:kuerzSubject41]
        isTrue[40] = 1
    if message2Value.find('0p') != -1:
        kuerzSubject[41] = message2Value.find('0p')+1
        kuerzSubject42 = message2Value.find('=', kuerzSubject[41], kuerzSubject[41]+30)
        mess2Val[41] = message2Value[kuerzSubject[41]:kuerzSubject42]
        isTrue[41] = 1
    if message2Value.find('0q') != -1:
        kuerzSubject[42] = message2Value.find('0q')+1
        kuerzSubject43 = message2Value.find('=', kuerzSubject[42], kuerzSubject[42]+30)
        mess2Val[42] = message2Value[kuerzSubject[42]:kuerzSubject43]
        isTrue[42] = 1
    if message2Value.find('0r') != -1:
        kuerzSubject[43] = message2Value.find('0r')+1
        kuerzSubject44 = message2Value.find('=', kuerzSubject[43], kuerzSubject[43]+30)
        mess2Val[43] = message2Value[kuerzSubject[43]:kuerzSubject44]
        isTrue[43] = 1
    if message2Value.find('0s') != -1:
        kuerzSubject[44] = message2Value.find('0s')+1
        kuerzSubject45 = message2Value.find('=', kuerzSubject[44], kuerzSubject[44]+30)
        mess2Val[44] = message2Value[kuerzSubject[44]:kuerzSubject45]
        isTrue[44] = 1
    if message2Value.find('0t') != -1:
        kuerzSubject[45] = message2Value.find('0t')+1
        kuerzSubject46 = message2Value.find('=', kuerzSubject[45], kuerzSubject[45]+30)
        mess2Val[45] = message2Value[kuerzSubject[45]:kuerzSubject46]
        isTrue[45] = 1
    if message2Value.find('0u') != -1:
        kuerzSubject[46] = message2Value.find('0u')+1
        kuerzSubject47 = message2Value.find('=', kuerzSubject[46], kuerzSubject[46]+30)
        mess2Val[46] = message2Value[kuerzSubject[46]:kuerzSubject47]
        isTrue[46] = 1
    if message2Value.find('0v') != -1:
        kuerzSubject[47] = message2Value.find('0v')+1
        kuerzSubject48 = message2Value.find('=', kuerzSubject[47], kuerzSubject[47]+30)
        mess2Val[47] = message2Value[kuerzSubject[47]:kuerzSubject48]
        isTrue[47] = 1
    if message2Value.find('0w') != -1:
        kuerzSubject[48] = message2Value.find('0w')+1
        kuerzSubject49 = message2Value.find('=', kuerzSubject[48], kuerzSubject[48]+30)
        mess2Val[48] = message2Value[kuerzSubject[48]:kuerzSubject49]
        isTrue[48] = 1
    if message2Value.find('0x') != -1:
        kuerzSubject[49] = message2Value.find('0x')+1
        kuerzSubject50 = message2Value.find('=', kuerzSubject[49], kuerzSubject[49]+30)
        mess2Val[49] = message2Value[kuerzSubject[49]:kuerzSubject50]
        isTrue[49] = 1
    if message2Value.find('0y') != -1:
        kuerzSubject[50] = message2Value.find('0y')+1
        kuerzSubject51 = message2Value.find('=', kuerzSubject[50], kuerzSubject[50]+30)
        mess2Val[50] = message2Value[kuerzSubject[50]:kuerzSubject51]
        isTrue[50] = 1
    if message2Value.find('0z') != -1:
        kuerzSubject[51] = message2Value.find('0z')+1
        kuerzSubject52 = message2Value.find('=', kuerzSubject[51], kuerzSubject[51]+30)
        mess2Val[51] = message2Value[kuerzSubject[51]:kuerzSubject52]
        isTrue[51] = 1
    #if message2Value.find('0[') != -1:
    #    kuerzSubject[52] = message2Value.find('0[')+1
    #    kuerzSubject53 = message2Value.find('=', kuerzSubject[52], kuerzSubject[52]+30)
    #    mess2Val[52] = message2Value[kuerzSubject[52]:kuerzSubject53]
    #    isTrue[52] = 1
    
    #n = 52
    #i = 0
    #while i <= n:
    #    if isTrue[i] == 1:
    #    i = i+1
    
    stelle = [ n for n, t in enumerate(isTrue) if t==1 ] 
    x = stelle
    sortiert = selection_sort(x)
    print(x)
    
    for i in range(len(sortiert)):
        var = sortiert[i]
        print(var)
        messSend.append(mess2Val[var])
        print(messSend)
        
    
    
    
    show_messages(textX, textY)
    
    messSend = []
    
    #UHR
    
    today = datetime.date.today()
    #print(today.day)
    #print(today.month)
    #print(today.year)

    weekdayVar = today.weekday()
    weekday = ' '

    if weekdayVar == 0:
        weekday = 'Montag'
    elif weekdayVar == 1:
        weekday = 'Dienstag'
    elif weekdayVar == 2:
        weekday = 'Mittwoch'
    elif weekdayVar == 3:
        weekday = 'Donnerstag'
    elif weekdayVar == 4:
        weekday = 'Freitag'
    elif weekdayVar == 5:
        weekday = 'Samstag'
    elif weekdayVar == 6:
        weekday = 'Sonntag'

    #print(weekday)

    timee = datetime.datetime.today()
    #print(timee.hour)
    hourValue = timee.hour
    #print(timee.minute)
    minuteValue = timee.minute
    if minuteValue == 1:
        minVal = '01'
    elif minuteValue == 2:
        minVal = '02'
    elif minuteValue == 3:
        minVal = '03'
    elif minuteValue == 4:
        minVal = '04'
    elif minuteValue == 5:
        minVal = '05'
    elif minuteValue == 6:
        minVal = '06'
    elif minuteValue == 7:
        minVal = '07'
    elif minuteValue == 8:
        minVal = '08'
    elif minuteValue == 9:
        minVal = '09'
    elif minuteValue >= 10:
        minVal = str(minuteValue)
    
    show_datetime(textX, textY)




    
    
    
    # finish off by updating our display
    pygame.display.update()
