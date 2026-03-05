from datetime import datetime


# now() method is used to
# get object containing
#ent date & time.

#Punctuation Conventions

now_method = datetime.now()
# strftime() method used to

#Resume

# create a string represer
# the current time.
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time :", currentTime)