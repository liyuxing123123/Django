#/python3

import yaml

obj1 = {'name': 'James', 'age': 20}
obj2 = ['Lily', 29]

with open('config2_yaml', 'w') as f:
    yaml.dump_all([obj1, obj2], f)

