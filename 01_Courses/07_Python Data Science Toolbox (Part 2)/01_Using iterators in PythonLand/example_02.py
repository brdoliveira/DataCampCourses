# enumerate() -> will allow us to add a counter to any iterable while the second function, zip, will allow us to stitch together an arbitrary number of iterables.
avangers = ['hawkeye','iron man','thor','quicksilver']
e = enumerate(avangers)
print(type(e))
e_list = list(e)
print(e_list)
print('-' * 20)

for index,value in enumerate(avangers):
    print(index,value)
print('-' * 20)

for index,value in enumerate(avangers, start=10):
    print(index,value)
print('-' * 20)

names = ['barton','stark','odinson','maximoff']
z = zip(avangers,names)
print(type(z))
z_list = list(z)
print(z_list)
print('-' * 20)

for z1,z2 in zip(avangers,names):
    print(z1,z2)
print('-' * 20)
print(*z) # unzip