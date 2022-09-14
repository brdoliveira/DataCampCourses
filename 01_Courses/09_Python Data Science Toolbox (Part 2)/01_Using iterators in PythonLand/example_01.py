# iter() -> creates an iterator
# next() -> produces next value

word = 'Da'
it = iter(word)
print(next(it)) # D
print(next(it)) # a

word = 'Data'
it = iter(word)
print(*it) # No more values to go through!

# Iterating over dictionaries
pythonistas = {'hugo':'bowne-anderson',
               'francis':'castro'}

for key,value in pythonistas.items():
    print(key,' : ',value)

# Iterating over file connections
file = open('./data/file.txt')
it = iter(file)
print(next(it))