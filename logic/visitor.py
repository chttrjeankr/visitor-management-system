import time
import datetime

import logic.emails as emails
import logic.database as database

class Visitor:
    def __init__(self,v,h):
        self.timestamp = int(time.time())
        self.visitor = v
        self.host = h
        self.check_times = {'check_in':None, 'check_out':None}

    def __del__(self):
        del self.visitor
        del self.host
        del self.timestamp
        del self.check_times

    def check_in(self):
        print("Checked In")
        self.check_times['check_in'] = datetime.datetime.now().strftime("%I:%M %p")
        database.update_time_in_database(self.timestamp, self.check_times)
        emails.send_email_to_host(self.timestamp)

    def check_out(self):
        print("Checked Out")
        self.check_times['check_out'] = datetime.datetime.now().strftime("%I:%M %p")
        database.update_time_in_database(self.timestamp, self.check_times)
        emails.send_email_to_visitor(self.timestamp)

    def submit_and_store(self):
        database.add_to_database(self.timestamp, self.visitor, self.host, self.check_times)
