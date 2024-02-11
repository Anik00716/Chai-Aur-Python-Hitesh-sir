type_of_pet = "Dog"
age_of_pet = 5

if type_of_pet == "Dog":
    if age_of_pet < 2:
        print("Please give Puppy food")
    else:
        print("Please give adult food")

elif type_of_pet == "Cat":
    if age_of_pet > 5:
        print("Please give senior cat food")
    else:
        print("Please give Junior cat food")
