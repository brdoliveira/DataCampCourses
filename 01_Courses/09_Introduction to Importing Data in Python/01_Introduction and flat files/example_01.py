
filename = './data/huck_finn.txt'
file = open(filename,mode='r') # 'r' is to read
                               # 'w' is to write
text = file.read()
file.close() # best practice
print(text)

with open(filename,'r') as file: # no need to close
    print(file.read())