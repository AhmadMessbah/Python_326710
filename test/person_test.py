from controller.person_controller import PersonController
from model.entity.person import Person
from model.repository.person_repository import PersonRepository
from model.service.person_service import PersonService

# Entity Test Passed
# person1 = Person("ali", "alipour", 40)
# print(person1)


# Repository Test Passed
# person_repo = PersonRepository()
# person_repo.save(person1)


# Service Test Passed
# PersonService.save(person1)


# Controller Test Passed
print(PersonController.save("ali1", "alipour", 20))