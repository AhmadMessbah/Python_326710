from model.repository.person_repository import PersonRepository


class PersonService:
    @classmethod
    def save(cls, person):
        if 20 <= person.age <= 30:
            person_repo = PersonRepository()
            person_repo.save(person)
        else:
            raise ValueError("Service Error : Age is not Ok !!!")

    # save/edit/remove/find_all/find_by_id
    # find_by_name - find_by_family - find_by_name_and_family
