import datetime

#function to get current date
def getDate():
    dt = datetime.datetime.now()
    return(dt.strftime("%x"))

#function to get current time
def getTime():
    dt = datetime.datetime.now()
    return(dt.strftime("%X"))

