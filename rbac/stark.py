from . import models
from stark.service import v1

class UserConfig(v1.StarkConfig):
    list_display = ['id','username','email']

v1.site.register(models.User,UserConfig)

class MenuConfig(v1.StarkConfig):
    list_display = ['id','title']


v1.site.register(models.Menu,MenuConfig)


class GroupConfig(v1.StarkConfig):
    list_display = ['id','caption']


v1.site.register(models.Group,GroupConfig)


class PermissionConfig(v1.StarkConfig):
    list_display = ['title','url','code','menu_gp','group']


v1.site.register(models.Permission,PermissionConfig)



class RoleConfig(v1.StarkConfig):
    list_display = ['id','title']


v1.site.register(models.Role,RoleConfig)



