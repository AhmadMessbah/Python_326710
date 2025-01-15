# id int
# name str
# write str
# pages int
import re



class Book:
    def __init__(self, name, write, pages):
        self.id = None
        self.name = name
        self.write = write
        self.pages = pages

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{2,30}$", value):
            self._name = value

        else :
            raise ValueError("Name can only contain alphanumeric characters")

    def __repr__(self):
        return f"Name : {self.name},Writer :{self.write},Pages :{self.pages}"