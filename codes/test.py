import datetime
now = datetime.datetime.now()
print now.year

# today_str=str(now.year)+'-'+str(now.month)+'-'+str(now.day)


today_str=now.strftime("%Y-%m-%d")
print today_str