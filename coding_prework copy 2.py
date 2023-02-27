#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    """ask the user for username"""
    user_name = input("Please type your name")
    """say hello to the user! :)"""
    print(f"Hello {user_name.upper()}, you got this in the bag! :)")

hello_name('ish')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    q2 = 1
    while True:
        if q2 < 99: 
            q2 += 2
            print(q2)
        else:
            break
 
first_odds()

#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. 

#def max_num_in_list(a_list):

#First im going to make sure i can to sort a list in order an pull the highest number. 
#Then I will add the code to my function, and place the list as my argument.  


def max_num_in_list(numbers_list):
    """sort the numbers from lowest to highest"""
    numbers_list.sort()
    """print the last number"""
    print(numbers_list[-1])
    
numbers_list = [1,2,3,4,11,6,7,8,10]
max_num_in_list(numbers_list)


numbers_list = [22,44,67,33,99,2,5]
max_num_in_list(numbers_list)

#Question 4:
#Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

#Use modulo operator to see if the year is divisible by 400, 100, and 4, in an if statement.
#If is, it should'nt have a remainder and it will be true. 
#If it has a remainder it will be false. 
#Then place that code in the body of the function.
#Use the input function to ask for a date and convert it to an integer. 
#Then plug in the recived value as the argument in the call function.  


def get_leap_year(leap_year):
    """Check to see if if you get a reminder when diving. If no remainder = true. If remainder = false"""
    if leap_year % 400 == 0:
        print(bool(1))  
    elif leap_year % 100 == 0:
        print(bool(1))
    elif leap_year % 4 == 0:
        print(bool(1))  
    else:
        print(bool(0))

leap_year = input("Please input leap year here: ")
leap_year = int(leap_year)
get_leap_year(leap_year)

#Queston 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.
 
#Create a function with a parameter whose argument will be a list. 
def check_numbers_numbers(numbers):
    """check if list is consecuitve order"""
    #Find the length of the list and set it to a new variable. 
    length_numbers= len(numbers)
    #Use a for loop with range function to loop through the list now that you have the length.
    #Make sure to subtract the list length by one since range starts at 0.
    for i in range(length_numbers - 1):
        #Add 1 to value of the number being pulled. Subtract that from same value being pulled. 
        #If it does not == 1 it’s False.
        if numbers[i + 1] - numbers[i] != 1:
            print("False")
        #If it == 1 its True.
        else:
            print("True")


numbers1 = [1,2,3,4,5,6]
numbers2 = [2,4,6,8,10]
check_numbers_numbers(numbers1)
check_numbers_numbers(numbers2)