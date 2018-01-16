from django.conf import settings
def init_permission(user,request):
    """
    初始化权限信息，获取权限信息并放置到session中。
    :param user:
    :param request:
    :return:
    """
    permission_list = user.roles.values('permissions__title',
                                        "permissions__code",
                                        "permissions__id",
                                        'permissions__url',
                                        'permissions__menu_gp_id',
                                        "permissions__group__id",
                                        "permissions__group__menu_id",
                                        "permissions__group__menu__title",
                                        ).distinct()
    menu_list=[]
    for item in permission_list:
        tpl={
            "id":item["permissions__id"],
            "title":item["permissions__title"],
            "menu_title":item["permissions__group__menu__title"],
            "url":item["permissions__url"],
            "menu_id":item["permissions__group__menu_id"],
            "menu_gp_id":item["permissions__menu_gp_id"],
        }
        menu_list.append(tpl)

    request.session[settings.PERMISSIONS_MENU_KEY]=menu_list



    # menu_list=[]
    # for item in permission_list:
    #     if not item["permissions__is_menu"]:
    #         continue
    #
    #     tpl={
    #         "menu_id":item["permissions__group__menu_id"],
    #         "menu_title":item["permissions__group__menu__title"],
    #         "title":item["permissions__title"],
    #         "url":item["permissions__url"],
    #         "active":False,
    #     }
    #
    #     menu_list.append(tpl)
    # print(menu_list)
    # request.session[settings.PERMISSIONS_MENU_KEY]=menu_list
     #权限管理
    result={}
    for item in permission_list:
        groupid=item["permissions__group__id"]
        code=item["permissions__code"]
        url=item["permissions__url"]

        if groupid in result:
            result[groupid]["codes"].append(code)
            result[groupid]["urls"].append(url)
        else:
            result[groupid]={
                "codes":[code,],
                "urls":[url,]
            }


    print(result)


    request.session[settings.PERMISSIONS_URL_DICT_KEY] = result