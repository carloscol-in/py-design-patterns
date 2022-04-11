class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'


class ResponsiblePerson:
  def __init__(self, person):
    self.person = person
    self.age = self.person.age

  # todo: rest of this class
  def _not_enough_age(self):
      return 'too young'

  def drink(self):
      if self.age < 18:
          return self._not_enough_age()
      return self.person.drink()

  def drive(self):
      if self.age < 16:
          return self._not_enough_age()
      return self.person.drive()

  def drink_and_drive(self):
      return 'dead'

if __name__ == '__main__':
    person1 = ResponsiblePerson(Person(10))
    person2 = ResponsiblePerson(Person(16))
    person3 = ResponsiblePerson(Person(15))
    person4 = ResponsiblePerson(Person(20))

    print(person1.drink())
    print(person1.drive())