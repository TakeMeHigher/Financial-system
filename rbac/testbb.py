import re
menu_list = [
    {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 2, 'title': '添加用户', 'url': '/userinfo/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 3, 'title': '删除用户', 'url': '/userinfo/del/(d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 4, 'title': '修改用户', 'url': '/userinfo/edit/(d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},

    {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 7, 'title': '删除订单', 'url': '/order/del/(d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 8, 'title': '修改订单', 'url': '/order/edit/(d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'}
]

current_url = "/userinfo/add/"
menu_dict={}
for item in menu_list:
    if not item["menu_gp_id"]:
        menu_dict[item["id"]]=item

    for item  in menu_list:
        url=item["url"]
        regex="^{0}$".format(url)

        if re.match(regex,current_url):
            menu_dict[item["menu_gp_id"]]["active"]=True

print(menu_dict)
'''

{
1: {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单管理', 'active': True},
5: {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单2'}}
'''
l=[]
for i in menu_dict.values():
    l.append(i)
print(l)
