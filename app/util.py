import datetime
import calendar

def _next_month():
	today = datetime.date.today()
	year = today.year + today.month / 12
	month = today.month % 12 + 1
	day = min(today.day, calendar.monthrange(year, month)[1])
	return datetime.date(year, month, day)