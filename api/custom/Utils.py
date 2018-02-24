import json
import datetime

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class DateUtil(Object):
    def __init__(self):
        self.shortDate = datetime.date.today()
        self.fullDate = datetime.datetime.today()

    def __str__(self):
        return self.shortDate

    def parseJSON(self):
        return "\\{ 'shortDate': {0}, 'fullDate': {1} \\}".format(self.shortDate, self.fullDate)
