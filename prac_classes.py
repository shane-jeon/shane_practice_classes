"""
Build a base class called AbstractPokemon that contains the following methods:
- __init__(self, name, lv=5)
- eat
- drink
- sleep

Build a Charmander class that inherits from the AbstractPokemon class that allows you to do the following:
- give it a nickname
- level up
- attack
- omnivore

Build a Charizard class that inherits from the Charmander class that allows you to:
- fly
- eats meat --> carnivore

Build a Squirtle class that inherits from the AbstractPokemon class that has the following methods:
- attack using water gun
- swim
- wears sunglasses
- herbivore
"""




# Build a base class called AbstractPokemon that contains the following methods:
# - __init__(self, name, lv=5)
# - eat
# - drink
# - sleep

class AbstractPokemon:
    def __init__(self, name, lv=5):
        # self.name = name
        self.n = name       # instance attribute "n" is bound to the value associated with the variable "name"
        self.level = lv
    
    def play(self):
        print("Yay! I'm playing!")

    def eat(self, dietary_status=""):
        """Give the Pokemon something to eat. Then it eats."""
        
        if dietary_status == "carnivore":
            print("Yum, I like eating meat. Thanks!")
        elif dietary_status == "herbivore":
            print("Yum, I like eating veggies. Thanks!")
        else:
            print("Yum, I like eating food. Thanks!")

        self.eat = eat
        self.drink = drink
        self.sleep = sleep


# Build a Charmander class that inherits from the AbstractPokemon class that allows you to do the following:
# - give it a nickname
# - level up
# - attack
# - omnivore   


class Charmander(AbstractPokemon):
    dietary_status = "omnivore"

    def eat(self):
        super().eat(self.dietary_status)



































# class Animal:
#     # (...snippet)

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     # (...snippet)


# class Cat(Animal):
#     # (...snippet)

#     def __init__(self, name):
#         super().__init__(name, 'cat')

#     # (...snippet)


# kitty = Cat("kitty")
# print(kitty.species)

# class Pokemon:
    













# class Animal:
#     print("Hello!")
#     info = "I am an animal"


#     def __init__(self, species):
#         self.species = "dog"
#         self.sound = 'bark'
#         self.is_cute = True

#     def speak(self, greet = "Hey there!"):
#         print(f"{greet} {self.info}. A {self.type} to be exact. My name is {self.name}.")

# class Cat(Animal):

#     def __init__(self,species):
#         # self.species = 'cat'

#         super().__init__(species, 'cat')

# kitty = Cat()
# print(kitty.species)

# jimmy = Animal("spotted")











# class Animal:
#     print('Hello!')
#     info ='I am an animal'

#     # def __init__(self, color):
#     #     self.color = color
#     #     self.is_cute = True

#     def speak(self):
#         print(f"{self.info}. A {self.type} to be exact. My name is {self.name}.")
    
#     def graduate(self):
#         self.speak() #accessing method from above (calling)
#         print(f'When I get my PhD, I will be Dr.{self.name}')
        

# jimmy = Animal()
# jimmy.speak()
        
# jimmy = Animal("spotted")
# print(jimmy)



# porter = Animal("dirty") #don't have to include is_cute in parameter because it is not called in instance parameter
# porter.type = "dog"
# porter.name = "Porter"
# porter.color = "white" #reassign


# porter.speak()
# porter.graduate()
# print(f"I am always {porter.color}")
# print(Animal.info)



##Other Example##

# class Animal:
#     species = "dog"


# class Dog:
#     has_fur = True

#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# dog = Dog("Sparky", "brown")

# new_dog = Dog("Bob", "white")

# print(dog.name, dog.color)
# print(dog.has_fur)
# print(dog.color)
# print(new_dog.color)

# dog.has_fur = False
# print(dog.has_fur, new_dog.has_fur)


##super classes##

# class Animal:
#     print('Hello!')
#     info ='I am an animal'

#     class Dog(Animal): 
#         info = "I am a dog" #overwrites parent class attribute

#         def sound(self):
#             print("Woof!")

#         def __init__(self):
#             self.fur_type = "I have fur."
#             self.ears = "I have ears."
#             self.tail = "I have a tail."

#     def __init__(self, color):
#         self.color = color
#         self.is_cute = True

#     def speak(self):
#         print(f"{self.info}. A {self.type} to be exact. My name is {self.name}.")
    
#     def graduate(self):
#         self.speak() #accessing method from above (calling)
#         print(f'When I get my PhD, I will be Dr.{self.name}')
    
        
# rogue = Dog

# print(rogue)