from datetime import date, datetime
import calendar

	
def Count_Sundays (First_Year, Last_Year):
	sundays = 0	
	for year in range (First_Year, Last_Year+1):
		for month in range (1, 13):
			if datetime(year, month, 1).weekday() == 6:
				sundays+=1
				
	print (sundays)		

Count_Sundays (1901, 2000)