class Person:
    def __init__(self, firstname, lastname, age, nationality, fav_color):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
        self.fav_color = fav_color

    def generate_person_entity(self):
        structure = {"first_name": self.firstname,
                     "last_name": self.lastname,
                     "age": self.age,
                     "favourite_colour": self.fav_color}
        return structure
