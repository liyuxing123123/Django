#/python3

#/python3



import json
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
import pygal_maps_world.maps
from Download_Data.country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # print(pop_data)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        # country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population
            # print(code + ": " + str(population))
        # else:
        #     print('ERROR - ' + country_name)
        # print(country_name + ": " + str(population))

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
# wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population2.svg')


