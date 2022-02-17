from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.views import View

from easytrade.models import Goods, Orders, Baskets
from easytrade.views.ViewMixIn import ViewMixIn


class BasketView(View, ViewMixIn):
    content = {}
    template_name = 'basket'
    basket = []
    order = Orders()

    def get(self, request):
        self.basket = request.session.get('basket', [])
        if self.basket:
            self.delete(int(request.GET.get('delete', -1)), request)
            self.format_basket()

        self.content['basket'] = self.basket
        return render(request, self.get_path(), self.content)


    def format_basket(self):
        for pid, item in enumerate(self.basket):
            item['pid'] = pid
            print(item)
            if not item['old']:
                item['good'] = Goods.objects.get(slug=item['good'])
                item['value'] = item['good'].end_price * float(item['number_of_goods'])

    def delete(self, item, session):
        if item == -1:
            return 0
        del self.basket[item]
        del session.session['basket'][item]
