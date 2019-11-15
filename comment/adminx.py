import xadmin

from .models import Comment,Message


class CommentAdmin:
    list_display = ['content', 'parent_comment', 'reply_to','create_time','author','post']
    list_filter = ['post', 'author']

    
xadmin.site.register(Comment,CommentAdmin)

class MessageAdmin:
    list_display = ['message_type','subject','content','file','create_time','author']
    list_filter = ['message_type', 'author']

xadmin.site.register(Message, MessageAdmin)

