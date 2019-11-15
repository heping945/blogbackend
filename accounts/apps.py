from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = '用户管理'

    # 与xadmin冲突，改回serializers save
    # def ready(self):
    #     import accounts.signals