from datetime import datetime

def get_days_from_today(date):
    try: 
        now = datetime.today()
        this_date=datetime.strptime(date, "%Y-%m-%d")
        difference = now - this_date
        return int(difference.days)
    except:
        print('Write the correct data! Format: YYYY-MM-DD')
        return None

ourDate='2024-10-01'
print(get_days_from_today(ourDate))
