from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

from easytrade.models import Goods, Orders
from easytrade.views.ViewMixIn import ViewMixIn


class SearchView(View, ViewMixIn):
    content = {}
    template_name = 'categories'

    def get(self, request):
        if not request.GET.get('find'):
            return redirect('home')
        self.set_pagination(request)
        self.set_menu()
        return render(request, self.get_path(), self.content)

    def set_pagination(self, request):
        good = Paginator(self.search_goods(request), 12)
        current_page = request.GET.get('page', 1)
        self.content['good'] = good.page(current_page)
        self.content['pages'] = good.page_range
        self.content['page_name'] = request.GET.get('find', '')

    def search_goods(self, request):
        search_string = request.GET.get('find', '')
        if search_string:
            return Goods.objects.filter(Q(search_queries__icontains=search_string) |
                                        Q(search_queries_ukr__icontains=search_string) |
                                        Q(title__icontains=search_string))
        else:
            return []

