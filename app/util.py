import datetime
import calendar

def _next_month():
	today = datetime.date.today()
	year = today.year + today.month / 12
	month = today.month % 12 + 1
	day = min(today.day, calendar.monthrange(year, month)[1])
	return datetime.date(year, month, day)

def _time(dateTime):
    hour=dateTime.hour
    minute=dateTime.minute
    if minute<10 :
        strminute = '0' + str(minute)
    else :
        strminute = str(minute)
    if hour>12 :
        mhour = (hour-12)
        return str(mhour) + ':'+ strminute + ' PM'
    elif hour==12 :
        return str(hour) + ':'+ strminute + ' PM'
    else :
        return str(hour) + ':'+ strminute + 'AM'