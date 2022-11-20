from django.contrib import admin
from .models import crud_post, Post, mutiple
# Register your models here.


admin.site.register([crud_post, Post, mutiple])
