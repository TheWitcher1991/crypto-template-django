from django.contrib import admin
from .models import Assets, Transactions, Users, Coin

admin.site.register(Transactions)
admin.site.register(Assets)
admin.site.register(Users)
admin.site.register(Coin)
