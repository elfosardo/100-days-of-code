from config import api

me = api.me()

print(me)

my_timeline = api.home_timeline(count=10)

print(my_timeline)
