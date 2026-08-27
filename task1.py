from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").toordinal()
        today=datetime.today().toordinal()
        return ((today-date))
    except:
        print("Wrong date format")
