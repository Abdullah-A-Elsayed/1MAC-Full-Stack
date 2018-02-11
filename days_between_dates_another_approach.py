# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def is_lower_date(date1,date2): #true if date1 is lower than 2
    if date1[0]<date2[0]: return True
    elif date1[0]==date2[0]:
        if date1[1]<date2[1]: return True
        elif date1[1]==date2[1]:
            if date1[2]< date2[2]:return True
            else: return False
        else: return False #m2 is higher
    else: return False #year 2 is lower
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    birth = (year1,month1,day1)
    now = (year2,month2,day2)
    days = 0
    while(is_lower_date(birth,now)):
        days+=1
        birth = nextDay(*birth)
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
