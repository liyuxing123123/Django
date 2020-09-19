#/python3

import pygal_maps_world.maps

vm = pygal_maps_world.maps.World()

vm.title = 'Populations of Countries in North America'

vm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

vm.render_to_file('na_populations.svg')


