from .Utils import Object

class Greeting(Object):
    def __init__(self, name="Stranger"):
        self.name = name
        self.message = "Hello {0}!!! How are you?".format(name)
