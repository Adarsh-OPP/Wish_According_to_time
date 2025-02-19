import time
currentTimes = time.strftime('%H:%M:%S')
currentTime = int(time.strftime('%H'))
print("Current time is:" , currentTimes)

if(currentTime >= 0 and currentTime <= 12 ):
    print("Good Moring")
elif(currentTime >= 13 and currentTime <= 19):
    print("Good Afternoon")
else:
    print('Good Evening')
