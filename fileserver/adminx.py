import xadmin

from .models import PostImg


class PostImgAdmin:
    list_display = ['name', 'img', 'imgMd5','created_time']

    
xadmin.site.register(PostImg,PostImgAdmin)


