# Task1 variable declaration
name = "Julie"

age = 44

sentence = f'Hi my name is {name} and I am {age} years old'
sentence2 = f'Hi my name is {name} and Iam too young: {age} years old'

todayIsCold = False

# if age > 40:
#     print(sentence)

# if todayIsCold:
#     print(sentence2)
# else:
#     print("today is cold")

# Task2 if/else
year = 2099

# if 2000 <= year < 2100:
#     print("Welcome to the 21st century!")
# else:
#     print("You are before or after the 21st century")

# Task3 functions


def tripleprint(string="exampleString"):
    # print('{}{}{}'.format(string,string,string))
    print(string*3)

# tripleprint()

# Task4 Lists

dogNames= ["Pupi","Chelo","Mufti"]

# for name in dogNames:
#     print(name)

# for x in range(0,11):
#     print(x)

age =0
# while age < 10:
#     print(age)
#     age+=1

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

# for x in numbers:
#     if x > 90:
#         print(x)


# Task5 Dictionary

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}
for i in range(1,len(words)):
    cooldictionary[words[i]] = definitions[i]
print(cooldictionary)
#Task 6 Classes

class Dog:
    def bark(self):
        print("BARK!")

myDog = Dog()
myDog.name = "Wuffi"
myDog.age = 12
myDog.bark()

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
       return 2020 - self.year

myCar = Car(1928,"Nissan","ProGT")

print(myCar.age())