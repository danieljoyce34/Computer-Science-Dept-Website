import datetime
import calendar
from app import app

def _next_month():
    today = datetime.date.today()
    year = today.year + today.month / 12
    month = today.month % 12 + 1
    day = min(today.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

def _get_time(datetime_obj):
    return str(datetime_obj.strftime('%I:%M%p'))

def _merge_two_dicts(dict1, dict2):
    newDict = dict1.copy()
    newDict.update(dict2)
    return newDict

def _append_to_dict(origin, list_to_append, name):
    origin[name] = list_to_append
    return origin

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']