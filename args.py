#list comprehension
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
print(squares)

#args
def total(*numbers):
    return sum(numbers)
print(total(1,2,3,4))

#*kwargs
def details(**data):
    for key, value in data.items():
        print(key, value)
details(name = "Hema", age = 21)

#return values
def square(x):
    return x * x
result = square(5)

#LEGB Rule
x = 100
def outer():
    x = 50
    def inner():
        x = 30
        print(x)
    inner()
outer()

#lambda
square = lambda x: x*x
print(square(5))
check = lambda x: "Even" if x % 2 == 0 else "Odd" #check with condition

#unstructured code
# a = 5
# b = 10
# return(a + b)
#structured code
def add(a, b):
    return a + b
def main():
    result = add(10,20)
    print(result)
main()

    