import datetime
#import datefinder
from flask import flash
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar.events'

# Contains helper functions to add events to calendar and parse text

def add_event(text):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    created_event = service.events().quickAdd(calendarId='primary', text=text).execute()
    return created_event

# def find_dates(text):
#     matches = datefinder.find_dates(text)
#     for match
#
# print(find_dates("MASS MEETING 1 Tuesday, September 11th 4:30-6:00 pm"))
