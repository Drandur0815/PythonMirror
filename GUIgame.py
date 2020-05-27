#!/usr/bin/env python

import pygame, sys
import datetime
import numpy as np
import imaplib
import email
from pygame.locals import *
import time
import requests






import configparser
 
def get_pw():
    config = configparser.ConfigParser()
    config.read('config.ini')
    returndata = (config['email']['username'], config['email']['password'], config['openweathermap']['apikey'])
    return returndata

username, password, api_key = get_pw()
location = 'Oberderdingen'


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

kuerzSubject = []
mess2Val = []
isTrue = []
messSend = []
list1 = [1, 20, 3]

minVal = '00'
    
font = pygame.font.Font('Roboto-Light.ttf',32)
    
textX = 5
textY = [0, 5, 55, 105]

def show_times(x,y):
    for i in range(0, len(uhrzeiten)):
	uhrz = font.render(str(uhrzeiten[i]), True, (150,250,250))
	screen.blit(uhrz, (x + i*100 - 10, y + 50))

def show_messages(x,y):
    message = font.render("From : " + mess1Val, True, (150,250,250))
    screen.blit(message, (x, y+100))
    #message2 = font.render("Subject : " + str(messSend), True, (255,255,255))
    #screen.blit(message2, (x, y+150))
    
def show_datetime(x,y):
    hour = font.render(str(hourValue), True, (150,250,250))
    screen.blit(hour, (x+380, y))
    minute = font.render(" : " + minVal, True, (150,250,250))
    screen.blit(minute, (x+410, y))


weather_timer = time.time()
mail_timer = time.time()

w, h = pygame.display.get_surface().get_size()
background_surface = pygame.Surface((w,h))

points = []
uhrzeiten = []
    
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

    if zeit >= weather_timer:
	zaehler1 = 0    
	wetter = []
	tag = []
	l = []
	sortedtemp = []
	color = (150,250,250)
#	start_pos = (500,500)
#	end_pos = (700,450)
	origin = (500, 500)
#	points = [(500, 500), (700, 400), (800, 450), (1000, 500)]
#	uhrzeiten = []
	temps_u_graph = []
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

	for j in range(0, 5):
	    leng = len(wetter[j])
	    l.append(leng)
	for h in range(0, l[0]):
	    temp_sort = wetter[0][h][0]
	    sortedtemp.append(float(temp_sort))
	try:
	    temp_sort = wetter[0+1][0][0]
	    sortedtemp.append(float(temp_sort))
	except Exception as _:
	    pass
	sortedtemp.sort()
	temp_min = sortedtemp[0]
	temp_max = sortedtemp[-1]
	print(temp_min)
	print(temp_max)
	for i in range(0, l[0]):
	    x_diag = origin[0]+(i)*100
#	    x_for_Temps.append(x_diag)
	    y_diag = origin[1]-((100/(temp_max-temp_min))*(wetter[0][i][0]-temp_min))
	    punkt = (x_diag, y_diag)
	    points.append(punkt)
	try:
	    x_diag = x_diag + 100
	    y_diag = origin[1]-((100/(temp_max-temp_min))*(wetter[0+1][0][0]-temp_min))
	    punkt = (x_diag, y_diag)
	    points.append(punkt)
	except Exception as _:
	    pass	

	#UHRZEITEN:
	current_tag = len(wetter[0])
	uhrzeiten.append(0)
	for i in range(0, current_tag):
	    uhrzt = 21 - i * 3
	    uhrzeiten.append(uhrzt)	
	uhrzeiten.reverse()
	print(uhrzeiten)

#	show_times(origin[0], origin[1])

	#TEMPERATUREN:
	for i in range(0, l[0]):
	    temps_u_graph.append(wetter[0][i][0])	
	temps_u_graph.append(wetter[0+1][0][0])
	print(temps_u_graph)

        #pygame.draw.line(background, color, start_pos, end_pos)
#	pygame.draw.lines(background, color, False, points)
	
#	print(x_for_Temps)	

        weather_timer = zeit + 60*10

#    show_times(origin[0], origin[1])
    if len(points) >= 2:
        pygame.draw.lines(background_surface, color, False, points)
    show_times(origin[0], origin[1])
        
    if zeit >= mail_timer:
        print('mail')
        mail_timer = zeit + 60*5
    
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
        mess1Val = message1Value[kuerzFrom1:kuerzFrom2]
    
        message2Value = email_message['Subject']
    
        show_messages(textX, textY[i])
    
    
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
    
    show_datetime(textX, textY[0])
    
    # finish off by updating our display
    pygame.display.update()
