### I've tried everything and I need help with the following in Python
###
###
### Create a Person class that has the following attributes. Make sure that these attributes are private:
### Name
### Age
### Date of Birth
###
### Create an __init__ method that takes these three attributes to create a Person class.
###
### Create a __str__ method so that you can print your class using print().
###
### Create mutator methods (getters and setters) to access these variables like:
### getName()
### getAge()
### getBirth()
### setName()
### setAge()
### setBirth()

# You cannot have both age and date of birth without entering a logical conflict. Therefore the age is calcualted uppon requset.
# However, I can easyly change this if you insist.


from datetime import datetime, date

class Person:
    def __init__(self, n, bd): # the date is expected in dd/mm/yyyy format
        self.__name = str(n)
        self.__date_of_birth = datetime.strptime(bd, '%d/%m/%Y')

    def __str__(self):
        return 'name = %s \ndate_of_birth = %s' %(self.__name, self.__date_of_birth.date())

    def getName(self):
        return self.__name

    def getAge(self):
        today = date.today()
        return today.year - self.__date_of_birth.year - ((today.month, today.day ) < (self.__date_of_birth.month, self.__date_of_birth.day))

    def getBirth(self):
        return self.__date_of_birth.date()

    def setName(self, n):
        self.__name = n
        return self

    # I haven't added setAge, as I cannot determin the birthdate based on specific ageself.

    def setBirth(self, bd):
        self.__date_of_birth = datetime.strptime(bd, '%d/%m/%Y')
        return self



if __name__ == '__main__':
    test_person = Person('John', '11/08/1983')
    print(test_person.getName())
    print(test_person.getAge())
    print(test_person.getBirth())
    print('Testing the set methods')
    test_person.setName('Sonja')
    test_person.setBirth('13/03/1988')
    print(test_person)
