#/python3

import yaml

aproject = {
    'name': 'Silenthand Ol',
    'race': 'Human',
    'traist': ['ONE_HAND', 'ONE_EYE']
}

f = open('config1.yaml', 'w')
print(yaml.dump(aproject,f))

