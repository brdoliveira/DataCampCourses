# Loop (For)

fam = [1.73,1.68,1.71,1.89]

# # Boring
# print(fam[0])
# print(fam[1])
# print(fam[2])
# print(fam[3])

# enumerate() --> produces the index and the value
for index,height in enumerate(fam): 
    print("index " + str(index) + ": " + str(height))    

for c in "famlily" :
    print(c.capitalize())
