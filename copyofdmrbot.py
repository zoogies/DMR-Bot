#make sure you have your client_secret.json in the same folder

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from groupy.client import Client
from datetime import date
import datetime
import calendar
import time
import requests
import schedule

i = 0

client = Client.from_token('replace this with your api token')
groups = list(client.groups.list_all())
group = groups[0]

xavier = 6
monty = 9
messer = 12
buckley = 15
luke = 18
zach_lewis = 21
eric = 24
kirk = 27
desilva = 30
stroh = 33
tommy = 36
anthony = 39
gilbert = 43
pease = 46
rj = 49
jay= 52
alsko = 55
tyler = 58
henry = 61
aj = 64
brayden = 67
difrangia = 70
hudson = 74
puhl = 77
zach = 80
roman = 83
ryan_z = 86
hand = 89
gabe = 92
torres = 95
whiteside = 98
ackley = 102
egolf = 105
schnipke = 108
wickham = 111
colton = 114
carter = 117
yosef = 120
jake = 123
zach_desilva = 126
ryan_c = 129
banks = 132
kafka = 135

slackers = ''
x = 0

def getunloggedlist(slackers,x):

    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]
    yesterday = ''

    '''
    monday > C 3
    tuesday > D 4
    wednesday > E 5
    thursday > F 6
    friday > G 7
    saturday > H 8
    sunday > I 9
    '''

    if today == 'Monday':
        yesterday = '3'
    if today == 'Tuesday':
        yesterday = '4'
    if today == 'Wednesday':
        yesterday = '5'
    if today == 'Thursday':
        yesterday = '6'
    if today == 'Friday':
        yesterday = '7'
    if today == 'Saturday':
        yesterday = '8'
    if today == 'Sunday':
        yesterday = '9'

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
    gspreadclient = gspread.authorize(creds)
    sheet = gspreadclient.open_by_url('replace this with your spreadsheet url')
    worksheet = sheet.get_worksheet(0)

    x = 0

    if worksheet.cell(xavier, yesterday).value == '':
        slackers = slackers + ', ' + ('xavier')
        x = x + 1
    if worksheet.cell(monty, yesterday).value == '':
        slackers = slackers + ', ' + ('monty')
        x = x + 1
    if worksheet.cell(messer, yesterday).value == '':
        slackers = slackers + ', ' + ('messer')
        x = x + 1
    if worksheet.cell(buckley, yesterday).value == '':
        slackers = slackers + ', ' + ('buckley')
        x = x + 1
    if worksheet.cell(luke, yesterday).value == '':
        slackers = slackers + ', ' + ('luke')
        x = x + 1
    if worksheet.cell(zach_lewis, yesterday).value == '':
        slackers = slackers + ', ' + ('zach lewis')
        x = x + 1
    if worksheet.cell(eric, yesterday).value == '':
        slackers = slackers + ', ' + ('eric')
        x = x + 1
    if worksheet.cell(kirk, yesterday).value == '':
        slackers = slackers + ', ' + ('kirk')
        x = x + 1
    if worksheet.cell(desilva, yesterday).value == '':
        slackers = slackers + ', ' + ('desilva')
        x = x + 1
    if worksheet.cell(stroh, yesterday).value == '':
        slackers = slackers + ', ' + ('Brain')
        x = x + 1
    if worksheet.cell(tommy, yesterday).value == '':
        slackers = slackers + ', ' + ('tommy')
        x = x + 1
    if worksheet.cell(anthony, yesterday).value == '':
        slackers = slackers + ', ' + ('anthony')
        x = x + 1
    if worksheet.cell(gilbert, yesterday).value == '':
        slackers = slackers + ', ' + ('nate gilbert')
        x = x + 1
    if worksheet.cell(pease, yesterday).value == '':
        slackers = slackers + ', ' + ('noah pease')
        x = x + 1
    if worksheet.cell(rj, yesterday).value == '':
        slackers = slackers + ', ' + ('rj')
        x = x + 1
    if worksheet.cell(jay, yesterday).value == '':
        slackers = slackers + ', ' + ('jay')
        x = x + 1
    if worksheet.cell(alsko, yesterday).value == '':
        slackers = slackers + ', ' + ('alsko')
        x = x + 1
    if worksheet.cell(tyler, yesterday).value == '':
        slackers = slackers + ', ' + ('tyler')
        x = x + 1
    if worksheet.cell(henry, yesterday).value == '':
        slackers = slackers + ', ' + ('henry')
        x = x + 1
    if worksheet.cell(aj, yesterday).value == '':
        slackers = slackers + ', ' + ('aj')
        x = x + 1
    if worksheet.cell(brayden, yesterday).value == '':
        slackers = slackers + ', ' + ('brayden')
        x = x + 1
    if worksheet.cell(hudson, yesterday).value == '':
        slackers = slackers + ', ' + ('alex hudson')
        x = x + 1
    if worksheet.cell(puhl, yesterday).value == '':
        slackers = slackers + ', ' + ('puhl')
        x = x + 1
    if worksheet.cell(zach, yesterday).value == '':
        slackers = slackers + ', ' + ('zach whitney')
        x = x + 1
    if worksheet.cell(roman, yesterday).value == '':
        slackers = slackers + ', ' + ('roman')
        x = x + 1
    if worksheet.cell(ryan_z, yesterday).value == '':
        slackers = slackers + ', ' + ('hackerman')
        x = x + 1
    if worksheet.cell(hand, yesterday).value == '':
        slackers = slackers + ', ' + ('nathan hand')
        x = x + 1
    if worksheet.cell(gabe, yesterday).value == '':
        slackers = slackers + ', ' + ('gabe')
        x = x + 1
    if worksheet.cell(torres, yesterday).value == '':
        slackers = slackers + ', ' + ('torres')
        x = x + 1
    if worksheet.cell(whiteside, yesterday).value == '':
        slackers = slackers + ', ' + ('whiteside')
        x = x + 1
    if worksheet.cell(ackley, yesterday).value == '':
        slackers = slackers + ', ' + ('ackley')
        x = x + 1
    if worksheet.cell(egolf, yesterday).value == '':
        slackers = slackers + ', ' + ('egolf')
        x = x + 1
    if worksheet.cell(schnipke, yesterday).value == '':
        slackers = slackers + ', ' + ('schnipke')
        x = x + 1
    if worksheet.cell(wickham, yesterday).value == '':
        slackers = slackers + ', ' + ('wickham')
        x = x + 1
    if worksheet.cell(colton, yesterday).value == '':
        slackers = slackers + ', ' + ('colton')
        x = x + 1
    if worksheet.cell(carter, yesterday).value == '':
        slackers = slackers + ', ' + ('carter')
        x = x + 1
    if worksheet.cell(yosef, yesterday).value == '':
        slackers = slackers + ', ' + ('yosef')
        x = x + 1
    if worksheet.cell(jake, yesterday).value == '':
        slackers = slackers + ', ' + ('jake')
        x = x + 1
    if worksheet.cell(zach_desilva, yesterday).value == '':
        slackers = slackers + ', ' + ('zach desilva')
        x = x + 1
    if worksheet.cell(ryan_c, yesterday).value == '':
        slackers = slackers + ', ' + ('Ryan C')
        x = x + 1
    if worksheet.cell(banks, yesterday).value == '':
        slackers = slackers + ', ' + ('Banks')
        x = x + 1
    if worksheet.cell(kafka, yesterday).value == '':
        slackers = slackers + ', ' + ('kafka')
        x = x + 1
    if worksheet.cell(difrangia, yesterday).value == '':
        slackers = slackers + ', ' + ('difrangia')
        x = x + 1
    print(slackers)
    print(x)
    if x > 0:
        message = str(x) + ' people did not log today. Dissapointing. They were' + slackers
        group.post(text=message)
        print(message)

    else:
        message = 'Literally everyone logged today! Good job boys remember to stay hydrated!'
        group.post(text=message)
        print(message)
def bruh():
    getunloggedlist(slackers,x)

schedule.every().day.at("20:15").do(bruh)

while True:
    schedule.run_pending()
    time.sleep(1)

