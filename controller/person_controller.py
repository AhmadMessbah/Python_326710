import re

from model.entity.person import Person
from model.service.person_service import PersonService


class PersonController:
    @classmethod
    def save(cls, name , family, age):
        try:
            person = Person(name, family, int(age))
            PersonService.save(person)
            return True, person
        except Exception as e:
            return False, f"{e}"

        # save/edit/remove/find_all/find_by_id
        # find_by_name - find_by_family - find_by_name_and_family