#/python3

import yaml

f = open('config.yaml')
y = yaml.load(f, Loader=yaml.FullLoader)
print(y)

