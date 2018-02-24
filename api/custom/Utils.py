import json
import datetime

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def dateToJSON(self, my_dictionary):
        return json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)

class DateUtil(Object):
    def __init__(self):
        self.shortDate = str(datetime.date.today())
        self.fullDate = str(datetime.datetime.today())
