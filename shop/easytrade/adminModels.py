from django.contrib import admin


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_trend', 'is_popular', 'is_published')
    list_editable = ('is_trend', 'is_popular', 'is_published')
    search_fields = ('title', 'category__name', 'price')


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'super_category')
    list_editable = ('super_category',)
