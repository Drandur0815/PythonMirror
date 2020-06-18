#!/usr/bin/env python

import pygame, sys
import datetime
import numpy as np
import imaplib
import email
from pygame.locals import *
import time
import requests
import simplenote
import paho.mqtt.client as mqtt





import configparser

def get_pw():
    config = configparser.ConfigParser()
    config.read('config.ini')
    returndata = (config['email']['username'], config['email']['password'], config['openweathermap']['apikey'], config['note_email']['user'], config['note_email']['password2'])
    return returndata

username, password, api_key, user, password2 = get_pw()
location = 'Oberderdingen'

sn = simplenote.Simplenote(user, password2)


def get_forecast(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()




pygame.init()

#screen = pygame.display.set_mode((500, 500), 0, 32)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

backgroundfile = "background.png"
mousefile = "mouse.png"

background = pygame.image.load(backgroundfile).convert()
mouse = pygame.image.load(mousefile).convert_alpha()

#BILDER LADEN:
bilder = []
im01db = pygame.image.load('Images/01d.png')
im01d = pygame.transform.scale(im01db, (50, 50))
bilder.append(im01d)
im01nb = pygame.image.load('Images/01n.png')
im01n = pygame.transform.scale(im01nb, (50, 50))
bilder.append(im01n)
im02db = pygame.image.load('Images/02d.png')
im02d = pygame.transform.scale(im02db, (50, 50))
bilder.append(im02d)
im02nb = pygame.image.load('Images/02n.png')
im02n = pygame.transform.scale(im02nb, (50, 50))
bilder.append(im02n)
im03db = pygame.image.load('Images/03d.png')
im03d = pygame.transform.scale(im03db, (50, 50))
bilder.append(im03d)
im03nb = pygame.image.load('Images/03n.png')
im03n = pygame.transform.scale(im03nb, (50, 50))
bilder.append(im03n)
im04db = pygame.image.load('Images/04d.png')
im04d = pygame.transform.scale(im04db, (50, 50))
bilder.append(im04d)
im04nb = pygame.image.load('Images/04n.png')
im04n = pygame.transform.scale(im04nb, (50, 50))
bilder.append(im04n)
im09db = pygame.image.load('Images/09d.png')
im09d = pygame.transform.scale(im09db, (50, 50))
bilder.append(im09d)
im10db = pygame.image.load('Images/10d.png')
im10d = pygame.transform.scale(im10db, (50, 50))
bilder.append(im10d)
im10nb = pygame.image.load('Images/10n.png')
im10n = pygame.transform.scale(im10nb, (50, 50))
bilder.append(im10n)
im11db = pygame.image.load('Images/11d.png')
im11d = pygame.transform.scale(im11db, (50, 50))
bilder.append(im11d)
im11nb = pygame.image.load('Images/11n.png')
im11n = pygame.transform.scale(im11nb, (50, 50))
bilder.append(im11n)
im13db = pygame.image.load('Images/13d.png')
im13d = pygame.transform.scale(im13db, (50, 50))
bilder.append(im13d)
im13nb = pygame.image.load('Images/13n.png')
im13n = pygame.transform.scale(im13nb, (50, 50))
bilder.append(im13n)
im50db = pygame.image.load('Images/50d.png')
im50d = pygame.transform.scale(im50db, (50, 50))
bilder.append(im50d)
im50nb = pygame.image.load('Images/50n.png')
im50n = pygame.transform.scale(im50nb, (50, 50))
bilder.append(im50n)



bilder_dict = {
    "01d" : 0,
    "01n" : 1,
    "02d" : 2,
    "02n" : 3,
    "03d" : 4,
    "03n" : 5,
    "04d" : 6,
    "04n" : 7,
    "09d" : 8,
    "10d" : 9,
    "10n" : 10,
    "11d" : 11,
    "11n" : 12,
    "13d" : 13,
    "13n" : 14,
    "50d" : 15,
    "50n" : 16,
}

kuerzSubject = []
mess2Val = []
isTrue = []
messSend = []
list1 = [1, 20, 3]

minVal = '00'
    
font1 = pygame.font.Font('Roboto-Light.ttf',32)
font2 = pygame.font.Font('Roboto-Light.ttf',15)
    
textX = 5
textY = 5
textY2 = 1000
notesX = 800
notesY = 1500



#def screensaver():
#    while True:
#
#	screen.fill(0,0,0))
#
#	for event in pygame.event.get():
#	    if event.type == QUIT:
#		pygame.quit()
#		sys.exit()
#            elif event.type == pygame.KEYDOWN and event.key == 27:
#            	pygame.quit()
#            	sys.exit()



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("adam_mqtt")

gesture = ''
day = 0
screensaver = False
screen_timer = time.time() + 60

def on_message(client, userdata, msg):
    global day
    global screensaver
    global screen_timer
    gesture = str(msg.payload) 
    print(gesture)
    if not 'NONE' in gesture:
	screen_time = time.time() + 60
    if 'FAR' in gesture:
	screensaver = False
    elif 'NEAR' in gesture:
	screensaver = True
    if not screensaver:
        if 'RIGHT' in gesture:
	    day = (day + 1) % 5 
	    print(day)
        elif 'LEFT' in gesture:
	    day = (day - 1) % 5
	    print(day)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.178.222", 1883, 60)

def show_times(x,y):
    for i in range(0, len(uhrzeiten)):
	uhrz = font1.render(str(uhrzeiten[i]), True, (150,250,250))	
	screen.blit(uhrz, (x + i*100 - 10, y + 120))
	uhr = font2.render("Uhr" ,True, (150,250,250))
	screen.blit(uhr, ((x + i*100 - 10) + 35, y + 120))

def show_temps(x,y):
    for i in range(0, len(temps_u_graph)):
	tug = font1.render(str(temps_u_graph[i]), True, (150,250,250))	
	screen.blit(tug, (x + i*100 - 10, y + 30))
	grad = font2.render("C" ,True, (150,250,250))
	screen.blit(grad, ((x + i*100 - 10) + 35, y + 30))

def show_current_temp(x,y):
    currtemp = font1.render(str(temps_u_graph[0]), True, (150,250,250))
    screen.blit(currtemp, (x + 170, y))
    grad2 = font2.render("C" ,True, (150,250,250))
    screen.blit(grad2, (x + 250, y))
    screen.blit(bilder[bilder_dict[icon_graph[0]]], (x + 270, y)) 
#    screen.blit(bilder[bilder_dict[icon_graph[i]]], (origin[0] + i*100-10, origin[1] + 300))

def show_temp_tage(x,y):
    for i in range(0, 4):
	temp_tag = font1.render(str(temp_tage[i]), True, (150,250,250))
	screen.blit(temp_tag, (x + 200, y + 300 + i*50))
        grad3 = font2.render("C" ,True, (150,250,250))
        screen.blit(grad3, (x + 250, y + 300 + i*50))
	screen.blit(bilder[bilder_dict[icon_tage[i]]], (x + 300, y + 300 + i*50))

def show_messages(x,y):
    for i in range(0, 3):
        message = font1.render(mess1Val[i], True, (150,250,250))
        screen.blit(message, (x, y + i*50))
    ueberschr = font1.render("Emails", True, (150,250,250))
    screen.blit(ueberschr, (x, y - 55))
    #message2 = font.render("Subject : " + str(messSend), True, (255,255,255))
    #screen.blit(message2, (x, y+150))
    
def show_datetime(x,y):
    hour = font1.render(str(hourValue), True, (150,250,250))
    screen.blit(hour, (x+985, y))
    minute = font1.render(" : " + minVal, True, (150,250,250))
    screen.blit(minute, (x+1015, y))

def show_Weekday(x, y):
    weekday1 = font1.render(str(weekday), True, (150,250,250))
    screen.blit(weekday1, (x, y))
    screen.blit(weekday1, (x + 900, y + 35))

def show_Weekdays(x, y):
    for i in range(0, 4):
	wkds = font1.render(str(weekdays[i]), True, (150,250,250))
	screen.blit(wkds, (x, y + 300 + i*50))
    ueberschr2 = font1.render("Woche", True, (150,250,250))
    screen.blit(ueberschr2, (x, y + 250))

def show_notes(x, y):
    head1 = font1.render(titel, True, (150,250,250))
    screen.blit(head1, (x, y))
    body1 = font2.render(inhalt, True, (150,250,250))
    screen.blit(body1, (x, y + 30))
    head2 = font1.render(titel2, True, (150,250,250))
    screen.blit(head2, (x, y + 130))
    body2 = font2.render(inhalt2, True, (150,250,250))
    screen.blit(body2, (x, y + 160))



weather_timer = time.time()
mail_timer = time.time()
notes_timer = time.time()

w, h = pygame.display.get_surface().get_size()
background_surface = pygame.Surface((w,h))

points = []
uhrzeiten = []
mess1Val = []
temp_tage = []
icon_tage = []
weekdays = []
    
while True:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == 27:
            pygame.quit()
            sys.exit()
    
    zeit = time.time()
 
    screen.blit(background_surface, (0,0))
    #screen.fill((0,0,0))
    #pygame.display.update()
    
    x,y = pygame.mouse.get_pos()
    
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2
    
    screen.blit(mouse, (x,y))
    
    #mein Versuch Text:
  
 
    #BEFEHLE WEMOS
    client.loop()
    if zeit >= screen_timer:
	screensaver = True

    #UNLOCK MIRROR
#    notelist_scr = sn.get_note_list(data = False, since = None)
#    scr_note_id = notelist_scr[0][2][u'key']
#    scr_note = sn.get_note(scr_note_id)
#    scr_note_content = scr_note[0][u'content']
#    kuerz_scr_titel = scr_note_content.find('\n')
#    scr_titel = scr_note_content[:kuerz_scr_titel]
#    pw_scr = len(scr_titel)
#    if pw_scr == 5:
#	print('locked')
#    elif pw_scr == 6:
#	print('unlocked')

 
    if zeit >= notes_timer:
        #NOTIZEN VIA SIMPLENOTE 
        notelist = sn.get_note_list(data = False, since = None)
	print(notelist)
        latest_note_id = notelist[0][0][u'key']
        note = sn.get_note(latest_note_id)
        note_content = note[0][u'content']
        #aufteilen in ueberschrift und inhalt:
        kuerz_titel = note_content.find('\n')
        titel = note_content[:kuerz_titel]
        print(titel)
        inhalt = note_content[kuerz_titel:]
        print(inhalt)

        sec_latest_note_id = notelist[0][1][u'key']
        note2 = sn.get_note(sec_latest_note_id)
        note2_content = note2[0][u'content']
        #aufteilen in ueberschrift und inhalt:
        kuerz_titel2 = note2_content.find('\n')
        titel2 = note2_content[:kuerz_titel2]
        print(titel2)
        inhalt2 = note2_content[kuerz_titel2:]
        print(inhalt2)

        notes_timer = zeit + 60*3

    show_notes(notesX, notesY)

    #NOTIZEN VIA SIMPLENOTE 
#    notelist = sn.get_note_list(data = False, since = None)
#    print(notelist)
#    latest_note_id = notelist[0][0][u'key']
#    note = sn.get_note(latest_note_id)
#    note_content = note[0][u'content']
#    print(note_content)
    #aufteilen in ueberschrift und inhalt:
#    kuerz_titel = note_content.find('\n')
#    titel = note_content[:kuerz_titel]
#    print(titel)
#    inhalt = note_content[kuerz_titel:]
#    print(inhalt)



    if zeit >= weather_timer:
	zaehler1 = 0    
	wetter = []
	tag = []
	l = []
	sortedtemp = []
	color = (150,250,250)
#	start_pos = (500,500)
#	end_pos = (700,450)
	origin = (5, 200)
#	points = [(500, 500), (700, 400), (800, 450), (1000, 500)]
#	uhrzeiten = []
	temps_u_graph = []
	icon_graph = []
#	points = []
	x_for_Temps = []
	y_for_Temps = origin[1]+100
#	x_for_Temps.append(origin[0])
#	points.append(origin)
        forecast = get_forecast(api_key, location)
	datumalt = forecast['list'][0]['dt_txt'].split(" ")[0]
        for date in forecast['list']:
            Temperatur = float(date['main']['temp'])
            Icon = str(date['weather'][0]['icon'])
            datum = date['dt_txt'].split(" ")[0]
	    if datum != datumalt:
		zaehler1 = zaehler1 + 1
	    if zaehler1 == 1 or zaehler1 == 9 or zaehler1 == 17 or zaehler1 == 25 or zaehler1 == 33: 
		wetter.append(tag)
		tag = []
	    tag.append([Temperatur, Icon]) 
	wetter.append(tag)
	print(wetter)

        weather_timer = zeit + 60*10

    l = []
    for j in range(0, 5):
        leng = len(wetter[j])
        l.append(leng)
    sortedtemp = []
    for h in range(0, l[day]):
        temp_sort = wetter[day][h][0]
        sortedtemp.append(float(temp_sort))
    try:
        temp_sort = wetter[day+1][0][0]
        sortedtemp.append(float(temp_sort))
    except Exception as _:
        pass
    sortedtemp.sort()
    temp_min = sortedtemp[0]
    temp_max = sortedtemp[-1]
    print(temp_min)
    print(temp_max)
    points = []
    for i in range(0, l[day]):
        x_diag = origin[0]+(i)*100
    #	    x_for_Temps.append(x_diag)
        y_diag = origin[1]-((100/(temp_max-temp_min))*(wetter[day][i][0]-temp_min))
        punkt = (x_diag, y_diag)
        points.append(punkt)
    try:
        x_diag = x_diag + 100
        y_diag = origin[1]-((100/(temp_max-temp_min))*(wetter[day+1][0][0]-temp_min))
        punkt = (x_diag, y_diag)
        points.append(punkt)
    except Exception as _:
        pass	

    #UHRZEITEN:
    uhrzeiten = []
    current_tag = len(wetter[day])
    uhrzeiten.append(0)
    for i in range(0, current_tag):
        uhrzt = 21 - i * 3
        uhrzeiten.append(uhrzt)	
    uhrzeiten.reverse()
    print(uhrzeiten)

    #	show_times(origin[0], origin[1])

    #TEMPERATUREN:
    temps_u_graph = []
    for i in range(0, l[day]):
        temps_u_graph.append(wetter[day][i][0])	
    temps_u_graph.append(wetter[day+1][0][0])
    print(temps_u_graph)

    #ICONS:
    icon_graph = []
    for i in range(0, l[day]):
        icon_graph.append(wetter[day][i][1])
    icon_graph.append(wetter[day+1][0][1])
    print(icon_graph)

#pygame.draw.line(background, color, start_pos, end_pos)
#	pygame.draw.lines(background, color, False, points)

#	print(x_for_Temps)	

    #WEITERE TAGE SEITLICH ANZEIGEN:
    temp_tage = []
    icon_tage = []
    for i in range(1, 5):
        temp_tage1 = wetter[i][5][0]
        temp_tage.append(temp_tage1)
        icon_tage1 = wetter[i][5][1]
        icon_tage.append(icon_tage1)


#    show_times(origin[0], origin[1])
    if len(points) >= 2:
        pygame.draw.lines(screen, color, False, points)
    show_times(origin[0], origin[1])
    show_temps(origin[0], origin[1])
    show_current_temp(origin[0], textY)
    show_temp_tage(origin[0], origin[1])

    pygame.draw.line(screen, color, (textX, textY+480), (textX+500, textY+480))

    #BILDER ZEIGEN:
#    screen.blit(im01d, (1300, 200))
#    screen.blit(im01n, (1300, 250))
#    screen.blit(im02d, (1300, 300))
#    screen.blit(im02n, (1300, 350))
#    screen.blit(im03d, (1300, 400))
#    screen.blit(im03n, (1300, 450))
#    screen.blit(im04d, (1300, 500))
#    screen.blit(im04n, (1300, 550))
#    screen.blit(im09d, (1300, 600))
#    screen.blit(im10d, (1300, 650))
#    screen.blit(im10n, (1300, 700))
#    screen.blit(im11d, (1300, 750))
#    screen.blit(im11n, (1300, 800))
#    screen.blit(im13d, (1300, 850))
#    screen.blit(im13n, (1300, 900))
#    screen.blit(im50d, (1300, 950))
#    screen.blit(im50n, (1300, 1000))

    #BILDER UNTERM GRAPH:
#    im = ['im']
    for i in range(0, len(icon_graph)):
	screen.blit(bilder[bilder_dict[icon_graph[i]]], (origin[0] + i*100-10, origin[1] + 70))
#    print("".join((im[0], icon_graph[0])))
        
    if zeit >= mail_timer:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username,password)

        mail.select("inbox")

        result, data = mail.uid('search',None, "ALL")

        inbox_item_list = data[0].split()

    
        for i in range(1, 4):
            numbr = inbox_item_list[-i]
        
            result2, email_data = mail.uid('fetch', numbr, '(RFC822)')

            raw_email = email_data[0][1]#.decode("utf-8")

            email_message = email.message_from_string(raw_email)
    
            message1Value = email_message['From']
            #TRY:
            kuerzFrom1 = message1Value.find('<')+1
            kuerzFrom2 = message1Value.find('>')
            mess1Val1 = message1Value[kuerzFrom1:kuerzFrom2]
	    mess1Val.append(mess1Val1)
    
            message2Value = email_message['Subject']
    
#            show_messages(textX, textY[i])

            mail_timer = zeit + 60*5
    
    pygame.draw.line(screen, color, (textX, textY2-20), (textX+700, textY2-20))
    show_messages(textX, textY2)

#    mail = imaplib.IMAP4_SSL("imap.gmail.com")
#    mail.login(username,password)

#    mail.select("inbox")

#    result, data = mail.uid('search',None, "ALL")

#    inbox_item_list = data[0].split()

    
#    for i in range(1, 4):
#        numbr = inbox_item_list[-i]
        
#        result2, email_data = mail.uid('fetch', numbr, '(RFC822)')

#        raw_email = email_data[0][1]#.decode("utf-8")

#        email_message = email.message_from_string(raw_email)
    
#        message1Value = email_message['From']
        #TRY:
#        kuerzFrom1 = message1Value.find('<')+1
#        kuerzFrom2 = message1Value.find('>')
#        mess1Val = message1Value[kuerzFrom1:kuerzFrom2]
    
#        message2Value = email_message['Subject']
    
#        show_messages(textX, textY[i])
    
    
    #most_recent = inbox_item_list[-1]

    #oldest = inbox_item_list[0]

    #result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')

    #raw_email = email_data[0][1]#.decode("utf-8")

    #email_message = email.message_from_string(raw_email)
    
    #message1Value = email_message['From']
    #TRY:
    #kuerzFrom1 = message1Value.find('<')+1
    #kuerzFrom2 = message1Value.find('>')
    #mess1Val = message1Value[kuerzFrom1:kuerzFrom2]
    
    #message2Value = email_message['Subject']
    
    #show_messages(textX, textY)
    
    #UHR
    
    today = datetime.date.today()
    #print(today.day)
    #print(today.month)
    #print(today.year)

    weekdayVar = (today.weekday() + day) % 7
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
    show_Weekday(origin[0], textY)

    #WEEKDAYS FOR THE FORECAST
    for i in range(1, 5):
	weekdayVar_new = weekdayVar + i
	if weekdayVar_new%7 == 0:
	    weekdayVar_new = 0
    	if weekdayVar_new == 0:
            weekdays1 = 'Montag'
    	elif weekdayVar_new%7 == 1:
            weekdays1 = 'Dienstag'
   	elif weekdayVar_new%7 == 2:
            weekdays1 = 'Mittwoch'
    	elif weekdayVar_new%7 == 3:
            weekdays1 = 'Donnerstag'
    	elif weekdayVar_new%7 == 4:
            weekdays1 = 'Freitag'
    	elif weekdayVar_new%7 == 5:
            weekdays1 = 'Samstag'
    	elif weekdayVar_new&7 == 6:
            weekdays1 = 'Sonntag'
	weekdays.append(weekdays1)

    show_Weekdays(origin[0], origin[1])
	

    timee = datetime.datetime.today()
    #print(timee.hour)
    hourValue = timee.hour
    if hourValue <= 9:
        hourValue = '0' + str(hourValue)
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
    
    pygame.draw.line(screen, color, (textX+800, textY+35), (textX+1200, textY+35))
    show_datetime(textX, textY)

    if screensaver:
	screen.blit(background_surface, (0,0))
    
    # finish off by updating our display
    pygame.display.update()
