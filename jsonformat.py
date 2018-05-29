import json
import argparse
import sys
import csv


class Person:
    def __init__(self, firstname, lastname, age, nationality, fav_color):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
        self.fav_color = fav_color


parser = argparse.ArgumentParser()
parser.add_argument('files', nargs=argparse.REMAINDER)
options = parser.parse_args()

person_list = []

if len(options.files) > 0:
    if len(options.files) > 1:
        print("This client takes exactly one file for processing. Taking first file \"{}\"".format(options.files[0]))
    file = open(options.files[0],'r')
else:
    file = sys.stdin

csvrecords = csv.DictReader(file)

for record in csvrecords:
    person = Person(record["first_name"],record["surname"],record["age"],record["nationality"],
                    record["favourite_colour"])
    person_list.append(person)


def generate_person_entity(entity: Person):
    format = {"first_name": entity.firstname, "last_name": entity.lastname, "age": entity.age, "favourite_colour": entity.fav_color}
    return format


person_entity_list = []

for person in person_list:
    record = generate_person_entity(person)
    person_entity_list.append(record)

json_person_entity = json.dumps({"person": person_entity_list}, indent=2)

print(json_person_entity)
