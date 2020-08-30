from data import people, plants_list, plants_dict

people = []
if bool(people) and all([person[1] for person in people]):  # returns true if all of the fields are not empty
    print("sending email")
else:
    print("user must edit the list of recipients")

# if any([plant.plant_type == "Grass" for plant in plants_list]):
#     print("This pack contains grass")
# else:
#     print("No grasses in this pack")


if any(plants_dict[plant].plant_type == "Grass" for plant in plants_dict):
    print("This dict contains grass")
else:
    print("No grasses in this dict")
