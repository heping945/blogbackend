import xadmin

from .models import Info


class InfoAdmin:
    list_display = ['id','title', 'body', 'create_date', 'mod_date', 'body_md']


xadmin.site.register(Info, InfoAdmin)






