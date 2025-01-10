import re


class Person:
    def __init__(self, name, family, age):
        self.id = None
        self.name = name
        self.family = family
        self.age = age


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{2,30}$", value):
            self._name = value
        else:
            raise ValueError("Invalid Name")
        
    def __repr__(self):
        return f"{self.name} {self.family} - {self.age}"


