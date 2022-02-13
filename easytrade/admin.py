import sys

from django.contrib import admin

import easytrade.models as mod
import easytrade.adminModels as adm


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_trend', 'is_popular', 'is_published')


admin_class = []
for klass in dir(adm):
    if not klass.startswith('__') and not klass.endswith('__') and klass.endswith('Admin'):
        admin_class.append(klass.replace('Admin',''))


for klass in dir(mod):
    if not klass.startswith('__') and not klass.endswith('__') and klass[0].isupper():
        if klass in admin_class:
            admin.site.register(
                getattr(mod, klass),
                getattr(adm, f'{klass}Admin')
            )
        else:
            admin.site.register(
                getattr(mod, klass),
            )


