#function without input
def greet():
    print("1st statement")
    print("2nd statement")
    print("3rd statement")
greet() 

#function with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")
nameinput="Vivek"
greet_with_name(nameinput)

#function with more than 1 input

def greet_with(name,location):
    print(f"Hello {name} from {location}")

greet_with("Vivek","Bhubaneshwar!")

#function with keyword arguments

def greet_with(name,location):
    print(f"Hello {name} from {location}")

greet_with(location="Bhubaneshwar!",name="Vivek")