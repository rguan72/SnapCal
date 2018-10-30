import datetime
import datefinder
from flask import flash
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar.events'

# Contains helper functions to add events to calendar and parse text
def dates_exist(text):
    matches = datefinder.find_dates(text)
    if not matches:
        print("No matches")
        return False
    else:
        print("Matches exist")
        return list(matches)


def add_event(text):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    created_event = service.events().quickAdd(calendarId='primary', text=text).execute()
    return created_event

text = """
First event is 10/18 at 5 pm.

Yo second event is 10/19 at 7 pm.

Third is 5 pm during October 10th
"""

# print(list(text.splitlines()))

def dates_exist(text):
    for line in list(text.splitlines()):
        if datefinder.find_dates(line):
            try:
                date = list(datefinder.find_dates(line))[0]
            except IndexError:
                continue
            print(line)
            print(date)

#print(datetime.datetime.strptime(text, '%x'))
# def find_dates(text):
#     matches = datefinder.find_dates(text)
#     for match
#
# print(find_dates("MASS MEETING 1 Tuesday, September 11th 4:30-6:00 pm"))
