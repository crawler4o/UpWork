### Create a Person class that has the attributes and method:
###
### Name
### Age
### Ethnicity
### Sex
###  __str__ method
###
### Remember that the __str__ method is how your class knows how to turn itself into a String. Without it, you won't be able to print your Person class correctly.
###
### Create a Person and print() the object. It should look something like:
###
### Example Output:
### Nam Nguyen, 24, Asian, Male
###
### After this, create a list of at least 5 Persons. Create a function that writes this list of people to a file, people.txt, on separate lines.
###
### Example:
### Yong Cheng, 24, Asian, Male
### Somebody Else, 33, Caucasian, Female
### Another Person, 26, African American, Male
### Yet Another Person, 40, Hispanic, Female

class Person:
    def __init__(self, name, age, ethnicity, sex):
        self.name = str(name)
        self.age = int(age)
        self.ethnicity = str(ethnicity)
        self.sex = str(sex)

    def __str__(self):
        return '%s, %s, %s, %s' %(self.name, self.age, self.ethnicity, self.sex)

def write_to_file(list):
    with open('people.txt', 'w') as open_file:
        for x in list:
            open_file.write('%s\n' % x)



if __name__ == '__main__':

    import names
    import random

    ethnicity_list = ['Asian', 'Caucasian', 'African American', 'Hispanic', 'European']
    persons_list = []

    for x in range(random.randrange(30)):
        gend = 'Female'
        if random.randrange(2):
            gend = 'Male'
        age = random.randrange(18, 79)
        name = names.get_full_name(gender = gend)
        ethnicity = ethnicity_list[random.randrange(5)]

        persons_list.append(Person(name, age, ethnicity, gend))


    write_to_file(persons_list)

    ### assen.georgiew@gmail.com
