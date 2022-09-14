'''
import json

with open('snake.json','r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))

for key,value in json_data.items():
    print(key+':'+value)
'''