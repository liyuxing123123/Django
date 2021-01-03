#/python3

import yaml

f = '''
---
name: James
age: 20
---
name: Lily
age: 19
'''

f1 = open('config.yaml')

y = yaml.load_all(f1,Loader=yaml.FullLoader)
for data in y:
    print(data)

