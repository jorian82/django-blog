from .Utils import Object

class Message(Object):

    def __init__(self, message, type, data):
        self.message = message
        self.type = type
        self.data = data

class CustomError(Message):

    def __init__(self, message):
        Message.__init__(self, message, "Error", Object())
