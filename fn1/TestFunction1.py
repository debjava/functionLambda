def check(input):
    print("Input Value : "+input)

def showAllAnimals(animalList):
    #check whether it is a List or not
    print("What kind of object is it ? ", type(animalList))
    for i in animalList:
        print("Animal is ", i)

check("Hello")
# animalList = ("Lion","Tiger","Rabbit") # Tuple
animalList = ["Lion","Tiger","Rabbit"] # List
showAllAnimals(animalList)
