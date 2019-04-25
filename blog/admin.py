from django.contrib import admin
from .models import Category,Tag,Post
# Register your models here.
class Postadmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Tag)