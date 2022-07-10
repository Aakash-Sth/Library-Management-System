from borrow import *
from returned import *
import datentime

n = 0
#loop for Library Management System
while True: 
    if (n != "a"):
        print("\t   Library Management System\n")
    print("-----------------------------------------------\n" +
          "|     Enter 1 to view the available books     |\n" +
          "|     Enter 2 to borrow books                 |\n" +
          "|     Enter 3 to return books                 |\n" +
          "|     Enter 4 to exit                         |\n" +
          "-----------------------------------------------")
    
    #exception handling
    while True:
        try:
            n = int(input("Enter a no.(1-4): "))
            break
        except:
            print("Please enter a whole no. from 1-4")        
        print("")
    print("")
    #codes for displaying books
    if (n == 1):
        printDetails("books.txt")
        
    #codes for borrowing book
    elif (n == 2):
        borrow()
                    
    #codes for returning book
    elif (n == 3):
        returned()
        
        
    #codes for validation   
    elif (n > 4 or n < 0):
        print("Please enter a valid no. from 1-4\n")
        n = "a"
        
    #code for exiting
    elif(n == 4):
        print("Thank you for using Library Management System!!!")
        break
        
        
        
              
                  
        





