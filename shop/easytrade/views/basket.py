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
        if request.GET.get('save'):
            self.save_basket(request.GET)
            self.content['basket'] = []
            request.session['basket'] = []
        else:
            for item in request.session.get('basket', []):
                order = Orders()
                order.good = Goods.objects.get(slug=item['good'])
                order.number_of_goods = int(item['number_of_goods'])
                request.session['basket'] = []
                order.save()
                self.basket.append(order)
            self.content['basket'] = self.basket
        self.set_menu()
        return render(request, self.get_path(), self.content)

    def save_basket(self, get):
        basket = Baskets()
        basket.telephone = get.get('telephone')
        basket.description = get.get('description') or ''
        basket.address = get.get('address')
        print(get)
        basket.save()
        for order in self.basket:
            basket.orders.add(order)

        basket.save()
