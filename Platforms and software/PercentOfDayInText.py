import time

# Get the current local time
local_time = time.localtime()

# Extract hour and minute
WrongHour = local_time.tm_hour
minute = local_time.tm_min


hour=WrongHour-5 #the timezone was off for my interpreter, so feel free to edit this alue according to your time. just make sure the current time it prints matches your current time.
print("Current Hour:", hour)
print("Current Minute:", minute)

# Convert hours to minutes and add current minutes
hourInMins = hour * 60
totalMins = hourInMins + minute

# Total minutes in a day
DayMins = 24 * 60

# Calculate percentage of the day completed
percent = (totalMins / DayMins) * 100

print(f"Amount of time one percent takes:{0.01*DayMins} minutes.")

print(f"Percentage of day completed: %{round(percent, 2)}")
