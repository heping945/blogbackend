import xadmin

from .models import Topic, Chapter


class TopicAdmin:
    list_display = ['title', 'urltag', 'reproduce', 'reproduce_source', 'desc']


xadmin.site.register(Topic, TopicAdmin)


class ChapterAdmin:
    list_display = ['title', 'topic', 'md5' , 'md_File', 'create_date','order']
    list_filter = ['topic', ]


xadmin.site.register(Chapter, ChapterAdmin)

