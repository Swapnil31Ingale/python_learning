import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp_hour = int(time.strftime('%H'))
print(timestamp_hour)
timestamp_minute = int(time.strftime('%M'))
print(timestamp_minute)
timestamp_second = int(time.strftime('%S'))
print(timestamp_second)

if (timestamp_hour >= 00 and timestamp_hour < 12):
    print("Good Morning Sir!!")
elif (timestamp_hour > 12 and timestamp_hour < 18):
    print("Goood Evenig Sir!!")
else:
    print("Good Night Sir!!")