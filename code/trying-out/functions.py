import math
def func_a(message):
    print(message)

def hypotenuse(a, b):
    if type(a) != type(1) or type(b) != type(1):
        return None 
    return math.sqrt(a + b)

def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder    

func_a('top kek')

b = func_a

func_a(b)

b('another one')

print(hypotenuse(4.0,966))

# you can do this11
q, r = divide(35, 4)
print(f'{q} {r}')

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(100))


def add_pet_to_list(pet, pets=[]):
    pets.append(pet)
    return pets

list_with_cat = add_pet_to_list("cat")
list_with_dog = add_pet_to_list("dog")

print(list_with_cat)
print(list_with_dog) # oops


def calculator(a, b, operator='+', output=float):
    if operator == '+':
        return output(a + b)
    if operator == '-':
        return output(a - b)        
    if operator == '*':
        return output(a * b)
    if operator == '/':
        if b == 0:
            print('You cannot divide by 0!')
        else:
            return output(a / b)

print(calculator(2,3.0,'/', int))


def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("%s: %s" % (k, v))

def print_args(*args):
    for arg in args:
        print(arg)


print_args("one", "two", "three")
print_args("one", "two", "three", "four")
print_kwargs(age=10)

my_dict = {"name": "Jane", "surname": "Doe"}
print_kwargs(**my_dict)



def args_calculator(operator, output=float, *args):
    result = 0
    if operator == '+':
        for arg in args:
            result += arg
        return output(result)
    if operator == '-':
        for arg in args:
            result -= arg
        return output(result + 2 * args[0])
    
            
print(args_calculator('-', float, 100,10,10,30))


