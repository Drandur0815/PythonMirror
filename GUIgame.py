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

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == 27:
            pygame.quit()
            sys.exit()
    
    zeit = time.time()
    zaehler1 = 0    
    datum = ''
    datumneu = ''
    datumalt = ''
    datum2 = ''
    datum3 = ''
    datum4 = ''
    datum5 = ''
    datum6 = ''
 
    #init done, now main part
    
    screen.blit(background, (0,0))
    #screen.fill((0,0,0))
    #pygame.display.update()
    
    x,y = pygame.mouse.get_pos()
    
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2
    
    screen.blit(mouse, (x,y))
    
    #mein Versuch Text:
    
    if zeit >= weather_timer:
        forecast = get_forecast(api_key, location)
	datum = forecast['list'][0]['dt_txt']
	datum1 = forecast['list'][0]['dt_txt']
        for date in forecast['list']:
            Temperatur = float(date['main']['temp'])
 	    datumalt = datum
            datum = date['dt_txt']
	    if datum != datumalt:
		datumneu = datum
		zaehler1 = zaehler1 + 1
	    if zaehler1 <= 8:
		datum2 = datumneu
	    if zaehler1 > 8 and zaehler1 <=16:
		datum3 = datumneu
	    if zaehler1 > 16 and zaehler1 <=24:
		datum4 = datumneu
	    if zaehler1 > 24 and zaehler1 <=32:
		datum5 = datumneu
	    if zaehler1 > 32 and zaehler1 <=40:
		datum6 = datumneu
       	    #print(Temperatur)
            #print(datum)
	#print(datum)
	print(datum1)
	print(datum2)
	print(datum3)	
	print(datum4)	
	print(datum5)	
	print(datum6)	
	#print(datumneu)
        weather_timer = zeit + 60*60
        
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
