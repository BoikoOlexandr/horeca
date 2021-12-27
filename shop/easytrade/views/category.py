from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from easytrade.models import Goods, Categories
from easytrade.views.ViewMixIn import ViewMixIn
from django.core.paginator import Paginator


class CategoryView(View, ViewMixIn):

    template_name = 'categories'

    def get(self, request, category):
        self.set_pagination(request, category)
        self.set_menu()
        return render(request, self.get_path(), self.content)

    def get_goods(self, cat):
        if not cat or cat == 'all':
            self.content['category_name'] = 'Всі товари'
            return Goods.objects.filter(is_published=True)
        else:
            cat = Categories.objects.get(name=cat)
            self.content['category_name'] = cat.name
            return Goods.objects.filter(is_published=True, category=cat)

    def set_pagination(self, request, category):
        good = Paginator(self.get_goods(category), 12)
        current_page = request.GET.get('page', 1)
        self.content['good'] = good.page(current_page)
        self.content['pages'] = good.page_range
