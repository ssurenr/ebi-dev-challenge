#!python

import json, argparse, sys, csv
from person import Person

# Extract filename from commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('files', nargs=argparse.REMAINDER)
options = parser.parse_args()

# File input mode
if len(options.files) > 0:
    if len(options.files) > 1:
        print("This client takes exactly one file for processing. Taking first file \"{}\"".format(options.files[0]))
    file = open(options.files[0],'r')
# User input mode
else:
    print("Enter data: Ctrl-D (i.e. EOF) to exit after entering return key")
    print("")
    file = sys.stdin

person_record_map = csv.DictReader(file)

person_list = []

for record in person_record_map:
    person = Person(record["first_name"],
                    record["surname"],
                    record["age"],
                    record["nationality"],
                    record["favourite_colour"])
    person_list.append(person)

person_entity_list = []

for person in person_list:
    person_entity_list.append(person.generate_person_entity())


json_person_entity = json.dumps({"person": person_entity_list}, indent=2)

print(json_person_entity)
