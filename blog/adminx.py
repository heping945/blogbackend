import xadmin

from .models import Category,Post,Tag


class CategoryAdmin:
    list_display = ['name', 'slug', 'parent_category']

    
xadmin.site.register(Category,CategoryAdmin)

class PostAdmin:
    list_display = ['title','excerpt','create_date','mod_date','views_count','codestyle',
                    'comment_count','can_comment','author','category','tags','reproduce']
    search_fields = ['title', 'body', 'create_date', 'category', 'author']
    list_filter = ['reproduce', 'category', 'author', 'tags','ifshow']
xadmin.site.register(Post, PostAdmin)

class TagAdmin:
    list_display = ['name','slug']
xadmin.site.register(Tag,TagAdmin)