from django.contrib import admin
from .models import Post,UserProfile,Comment,Notification,ThreadModel1

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(ThreadModel1)