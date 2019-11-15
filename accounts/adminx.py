import  xadmin
from xadmin import views

from .models import UserProfile

# 使用主题功能
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSettings)


class CustomView(object):
    site_title = '后台管理'  # 网页头部导航
    site_footer = 'copyright@hp 1970-2019'  # 底部版权内容
    menu_style = 'accordion'  # 左侧导航折叠框


xadmin.site.register(views.CommAdminView, CustomView)

class UserProfileAdmin(object):
    list_display = ['id','username', 'nickname', 'gender', 'address', 'phone', 'desc', 'avatar','headline','urltoken']
    search_fields = ['username', 'gender', 'address', 'desc', 'avatar']
    list_filter = ['username', 'gender',  'desc', 'avatar']

# 系统默认配置user表
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)