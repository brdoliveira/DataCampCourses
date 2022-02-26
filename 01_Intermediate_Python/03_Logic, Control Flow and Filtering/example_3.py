# if, elif, else

z = 6 
if z % 2 == 0: #True
    print("checking " + str(z))
    print("z is divisible by 2")
elif z % 3 == 0: # Never reached
    print("z is divisible by 3")
else:
    print("z is neither divisible by 2 nor by")