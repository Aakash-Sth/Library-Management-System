from datentime import *
import os

def printDetails(fname):
    file = open(fname,"r")
    print(file.read())
    file.close()

def readFile(fname):
    file = open(fname,"r")
    a = file.readlines()
    file.close()
    return a
    
#function for checking and changing the stock of borrowed book
def borrow():
    ct = 1
    count2 = 1
    ct3 = 0
    total = 0
    book = []
    bo = "Y"
    while True:
        if (count2 == 1 and ct3 == 0):
            #validation
            while True:                    
                name = input("Enter your name: ").upper()
                if (name.isalpha()):
                    break
                else:
                    print("You can't enter no. in name.")
            print("")
        print("--------------------------------------------------\n" +
              "|     Enter 1 to borrow Harry Potter             |\n" +
              "|     Enter 2 to borrow Start With Why           |\n" +
              "|     Enter 3 to borrow A Brief History of Time  |\n" +
              "|     Enter 4 to borrow Death By Black Hole      |\n" +
              "--------------------------------------------------")
        
        while True:
            #exception handling
            try:
                c = int(input("Enter a no.(1-4): "))
                print("")
                break
            except:
                print("Please enter a no.\n")
        
        

        ct3 = 0
        if (c == 1):
            bname = "Harry Potter"
        elif (c == 2):
            bname = "Start With Why"
        elif (c == 3):
            bname = "A Brief History of Time"
        elif (c == 4):
            bname = "Death By Black Hole"
        else:
            print("Please enter a no. from 1-4")
            ct3 = 1
            

        #validation
        count = 0
        for bk in book:
            if(bname == bk):
                print("You can't borrow same book twice.")
                count = -1
        
        if (ct3 == 0):
            filet = open("tid.txt","r")
            tid = filet.read()
            filet.close()
            p = os.path.abspath("Borrowers/Borrower_"+tid+"-"+name+".txt")
            
            if (count == 0):
                if (ct == 1):
                    details = ("Transaction ID: "+ tid + "\n" +"Borrower name: "+name +"\n"+
                        "Borrowing Date: "+ getDate()+"     "+
                       "Borrowing Time: "+getTime()+"\n\n"+
                       "S.N: "+"1\n"+
                       "Borrowed book: "+bname+
                       "\nPrice: ")
                    
                elif (ct > 1):
                    details = ("\n\nS.N: "+str(ct)+"\n"+
                       "Borrowed book: "+bname+
                       "\nPrice: ")

                c = ""    
                a = readFile("books.txt")
                count1 = 0
                for i in a:
                    b = i.replace("\n","").split(",")
                    
                    if (b[0] == bname and int(b[2]) > 0):
                        b[2] = int(b[2]) - 1
                        details += b[3]
                        total += int(b[3].replace("Rs",""))
                        count1 = 1
                    ct2 = 0        
                    for j in b:
                        c += str(j)
                        if (ct2 == 3):
                            break
                        c += ","
                        ct2 += 1
                    c +="\n"                    
                
                file = open("books.txt","w")
                file.write(c)
                file.close()                
                if (count1 == 0):
                    print("Sorry, the book is out of stock.")
                else:                    
                    if (ct == 1):
                        file = open(p,"w")
                        file.write("\t\t   Borrowing Details\n\n")
                    else:        
                        file = open(p,"a")
                    file.write(details)
                    file.close()
                    print("You have successfully borrowed",bname,"\n")
                
                if (count1 != 0):
                        ct += 1
                        book.append(bname)
                count2 += 1   
                
            while True:
                bo = input("Do you want to borrow other books(Y/N)? ").upper()
                print("")
                
                #validation
                if (bo != "Y" and bo != "N"):
                        print("Please enter Y or N")
                else:
                    break
            if(bo == "N"):
                break
            
    if (ct3 == 0):
        fileA = open(p,"a")
        fileA.write("\n\nTotal Price: Rs "+ str(total)+"\n\n"+
                    "\t\t***Thank you for borrowing***\n")
        fileA.close()        
        printDetails(p)
        
    filet = open("tid.txt","w")
    filet.write(str(int(tid)+1))
    filet.close()


    
    
    
    


