from django.contrib import admin
from django.db import models

from .models import MylistTitle, MylistGenre, MylistProduction, MylistYear, MylistQuarter
# Register your models here.


class addnewtitle(admin.ModelAdmin):

    fieldsets = [
        ('options', {'fields':['genre', 'production', 'year', 'quarter']}),
        ('contents', {'fields':['title', 'summary', 'title_img']}),
        ('url', {'fields':['title_slug']}),
    ]

admin.site.register(MylistTitle, addnewtitle)
admin.site.register(MylistGenre)
admin.site.register(MylistProduction)
admin.site.register(MylistYear)
admin.site.register(MylistQuarter)
