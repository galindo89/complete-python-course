import time

def power (limit):

    return [x**2 for x in range(limit)]

start=time.time() #current time

power(500000)

end=time.time() #current time

print(end-start)