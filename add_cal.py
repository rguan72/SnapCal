import datetime
import datefinder
from flask import flash
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class EventAdder(object):
    # ---------------
    # Contains helper functions to add events to calendar and parse text
    # --------------
    SCOPES = 'https://www.googleapis.com/auth/calendar.events'

    @classmethod
    def add_event(self, date, text):
        # Given a date and text, adds event to calendar
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))
        created_event = service.events().insert(calendarId='primary', event=event).execute()
        return created_event

    @classmethod
    def give_events(self, text):
        events = []
        for line in list(text.splitlines()):
            if datefinder.find_dates(line):
                try:
                    date = list(datefinder.find_dates(line))[0]
                except IndexError:
                    continue
                events.append({'summary' : line, 'start' : date, 'end' : date})
        return events

# text = """
# First event is 10/18 at 5 pm.
#
# Yo second event is 10/19 at 7 pm.
#
# Third is 5 pm during October 10th
# """
#
# events = EventAdder().give_(text)
# print(events)
