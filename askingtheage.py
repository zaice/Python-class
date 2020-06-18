# Goal: To ask how old the person.

a = input("How old are you? ")
print(type(a))
a = int(a)
print(type(a))

if a <= 5:
    print("You should go to the nursery-school!")
elif a >= 6 and a <= 17:
    print("Go to school and study well!")
elif a >= 18 and a <= 23:
    print("You need to get a job!")
elif a >= 24 and a <= 64:    
    print("Relaxxx, you got a job, now all you need is to get promoted!")  
else:
    print("Sorry, there was an error, try again!")        
