#/python3

class StarkConfig(object):

    def __init__(self,num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

class RoleConfig(StarkConfig):

    def changelist(self, request):
        print('666')

config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)

