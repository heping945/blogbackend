import xadmin

from .models import UserVote, UserFav


class UserVoteAdmin:
    list_display = ['user', 'post','vote', 'add_time',]
    list_filter = ['user', 'post',]


xadmin.site.register(UserVote, UserVoteAdmin)


class UserFavAdmin:
    list_display = ['user', 'post','add_time',]
    list_filter = ['user', 'post', ]

xadmin.site.register(UserFav, UserFavAdmin)

