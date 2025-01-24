#import secrets

#apiKey=secrets.token_urlsafe(16)
#print(apiKey)
from datetime import datetime, timedelta

curr_date=datetime.today()
next_week=curr_date + timedelta(days= 7- curr_date.weekday() )

print(next_week)