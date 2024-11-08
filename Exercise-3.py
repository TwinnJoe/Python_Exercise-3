# Question 1: Basic Function Definition and Calling

def greet():
    print ("Hello,World")

greet()



# Question 2: Function with Parameters

def personalized_greeting(name):
    print("Good morning "+name)

personalized_greeting(input("Name: "))



# Question 3: Function with Return Value

def square(number):

    return number * number

print("Square =", square(5))



# Question 4: Function with Multiple Parameters and Return Value

def rectangle_area(length, width):

    return length * width

print("Area =", rectangle_area(4,5))



# Question 5: Using a Function as an Argument

def apply_operation(operation, number):

    return operation(number)

def double(number):
    return number * number

print(apply_operation(double,7))

print(apply_operation(square,3))










