from borrow import *
from datentime import *

#function for calculating fine
def fine(name,p):
    file = open(p,"r")
    a = file.readlines()
    for b in a:
        c = b.split(" ")
        for d in range(len(c)-1):
            if (c[d] == "Date:"):
                bdate = c[d+1]
    file.close()
    s = bdate.split("/")
    month = int(s[0])
    day = int(s[1])
    date = getDate().split("/")
    cmonth = int(date[0])
    cday = int(date[1])
    if (month == cmonth):
        tdays = cday - day
    elif ((cmonth-month) == 1):
        tdays = (30-day)+ cday
    fine = 0
    if (tdays > 10):
        days = tdays - 10
        fine = days*20
        
    return fine
    
#function for changing the stock of the returned book     
def returned():
    while True:                    
        name = input("Enter your name: ").upper()
        if (name.isalpha()):
            break
        else:
            print("You can't enter no. in name.\n")
        
    while True:
        try:
            tid = int(input("Enter transaction Id:"))
            print("")
            break
        except:
            print("You can't enter alphabets in transaction ID\n")
   
    tid = str(tid)
    
    details = ("\t\t   Returning Details\n\n" +
               "Transaction ID: " + tid + "\n" +
               "Borrower name: " +name + "\n"+
               "Returning Date: " + getDate() + "     " + "Returning Time: " + getTime() + "\n")
    ap = os.path.abspath("Returned/Returned_" + tid + "-" + name + ".txt")
    p = os.path.abspath("Borrowers/Borrower_" + tid + "-" + name + ".txt")
    ct = 0
    
    if (os.path.exists(ap)):
        print("You have already returned the books.\n")
        ct = 1
    else:
        try:            
            a = readFile(p)
            c = 0
            for b in a:
                if (c >= 5 and c < (len(a) - 3)):
                   details += b
                elif (c == (len(a) - 3)):
                    details += " " + b
                c += 1
                if (c == (len(a) - 2)):
                    d = b.split(": Rs")
                    total = int(d[1].replace("\n",""))
        except:
            print("You haven't borrowed any books yet or you have entered wrong data.\n")
            ct = 1
        
    if (ct == 0):
        data = ""
        file = open(p,"r")
        a = file.readlines()
        book = []
        
        for b in a:
            c1 = b.split(": ")
            for i in range(len(c1)-1):
                if (c1[i] == "Borrowed book"): 
                    book.append(c1[i+1].replace("\n",""))
        file.close()

        for bn in book:
            data =""        
            a = readFile("books.txt")
            
            for i in a:
                b = i.replace("\n","").split(",")
                if (b[0] == bn):
                    b[2] = int(b[2]) + 1
                ct = 0
                for j in b:
                    data += str(j)
                    if (ct == 3):
                        break
                    data +=","
                    ct += 1
                data +="\n"
            
            file = open("books.txt","w")
            file.write(data)
            file.close()    
        
        
        c += 1
        fileA = open(ap,"w")
        fileA.write(details)
        Fine = fine(name,p)
        tamt = str(total+Fine)
        fileA.write("\tFine: " + "Rs "+ str(Fine)+
                    "\nTotal Amount: Rs " + tamt + "\n")
        
        if (Fine != 0):
            fileA.write("\nNote: Fines are applied if you exceed 10 days of borrowing.\n")
        fileA.close()
        
        printDetails(ap)
    
            
