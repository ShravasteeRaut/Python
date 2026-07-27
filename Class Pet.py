class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def display_profile(self):
        print("Pet Profile")
        print("Name :", self.name)
        print("Type :", self.animal_type)
        print("Age  :", self.age, "years")

pet1 = Pet("Buddy", "Dog", 3)
pet2 = Pet("Mittens", "Cat", 2)

pet1.display_profile()
print()
pet2.display_profile()















