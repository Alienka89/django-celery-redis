from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from .models import *


class BlockAdminLine(StackedInline):
    model = Block
    list_display = ('title', 'order_number', 'counter')
    extra = 0

    fieldsets = (
        ('Данные блока',
         {'fields': ('title', 'order_number', 'counter'), }
         ),
        ('text',
         {'fields': ('text',), }
         ),
        ('audio',
         {'fields': ('audio', 'bitrate',), }
         ),
        ('video',
         {'fields': ('video', 'video_sub',), }
         ),
    )


class PageAdmin(ModelAdmin):
    search_fields=('title','block__title')
    list_display = ('title', 'order_number',)
    list_editable = ('order_number',)
    inlines = [BlockAdminLine, ]


admin.site.register(Page, PageAdmin)
