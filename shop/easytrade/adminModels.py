from django.contrib import admin


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_trend', 'is_popular', 'is_published')
    list_editable = ('is_trend', 'is_popular', 'is_published')
    search_fields = ('title', 'category', 'price')


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
