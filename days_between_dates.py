# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if((year%4==0 and year%100!=0) or (year%400==0)): return True
    return False

def daysFrom1900(y,m,d):
	days = 0
	for year in range(1900,y):
		if isLeapYear(year):
			days+=366
		else:
			days+=365

	for month in range(1,m):
		if (isLeapYear(y) and (month == 2)):
			days+=1
		days+=daysOfMonths[month-1]

	days= days+d-1
	return days

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    dur1 = daysFrom1900(y1,m1,d1)
    dur2 = daysFrom1900(y2,m2,d2)
    return dur2-dur1

# print isLeapYear(2016)
# print isLeapYear(2100)
# print isLeapYear(2400)
print daysBetweenDates(2012,2,28,2012,2,29)