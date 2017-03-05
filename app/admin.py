from django.contrib import admin
from .models import Item,Comment,Likes,Unlike

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Unlike)
