import  re
from django.conf import settings
from django.template import Library
register = Library()
@register.inclusion_tag("menuList.html")
def menu_html(request):
    menu_list=request.session.get(settings.PERMISSIONS_MENU_KEY)
    currenturl=request.path_info

    menu_dict={}
    for item in menu_list:
        if not item["menu_gp_id"]:
            menu_dict[item["id"]]=item
    for item in menu_list:
        regex="^{0}$".format(item["url"])
        if re.match(regex,currenturl):
            menu_gp_id=item["menu_gp_id"]
            if not menu_gp_id:
                menu_dict[item["id"]]["active"]=True
            else:
                menu_dict[item["menu_gp_id"]]["active"]=True
    '''
    menu_dict={
    1: {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单管理', 'active': True},
    5: {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单2'}}
    '''

    result = {}
    for item in menu_dict.values():
        menu_id=item["menu_id"]
        menu_title=item["menu_title"]
        active=item.get("active")
        url=item["url"]
        title=item["title"]

        if menu_id in result:
            result[menu_id]["children"].append({"title":title,"url":url,"active":active})
            if active:
                result[menu_id]["active"]=True
        else:
            result[menu_id]={
                "menu_id":menu_id,
                "menu_title":menu_title,
                "active":active,
                "children":[
                    {"title":title,"url":url,"active":active},
                ]

            }



    # for item in menu_list:
    #     menu_id=item["menu_id"]
    #     menu_title=item["menu_title"]
    #     title=item["title"]
    #     url=item["url"]
    #     active=False
    #     regex="^{0}$".format(url)
    #     if re.match(regex,currenturl):
    #         active=True
    #
    #     if menu_id in result:
    #         result[menu_id]["children"].append({{"title":title,"url":url,"active":active},})
    #         if active:
    #             result[menu_id]["active"]=active
    #     else:
    #         result[menu_id]={
    #             "menu_id":menu_id,
    #             "menu_title":menu_title,
    #             "active":active,
    #             "children":[
    #                 {"title":title,"url":url,"active":active},
    #             ]
    #         }
    # print(result)

    return {"menu_dict":result}
