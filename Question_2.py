#Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string
#from the user and print_String print the string in upper case
#string will be an input to a get_string method and whatever you put in will print when you make the print screen method

class IOString():
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input()
        
    def print_String(self):
        print(self.str1.upper())
        
str1 = IOString()
str1.get_String()
str1.print_String()