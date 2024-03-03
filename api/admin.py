from django.contrib import admin

from api.models import User, Post, Comment, Like

admin.site.register([User, Post, Comment, Like])
