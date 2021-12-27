from django.contrib import admin

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_trend', 'is_popular', 'is_published')
    list_editable = ('is_trend', 'is_popular', 'is_published')
    search_fields = ('title',)
