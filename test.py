###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    day+=1
    if(day>30):
        day-=30
        month+=1
    if(month>12):
        month-=12
        year+=1
    return year,month,day
    
nex = nextDay(2012,12,30)+"hi"
print nex
### tuples are not strings and are not mutant

def is_lower_date(date1,date2): #true if date1 is lower than 2
    if date1[0]<date2[0]: return True
    elif date1[0]==date2[0]:
        if date1[1]<date2[1]: return True
        elif date1[1]==date2[1]:
            if date1[2]< date2[2]:return True
            else: return False
        else: return False #m2 is higher
    else: return False #year 2 is lower
        