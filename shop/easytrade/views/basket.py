from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.views import View

from easytrade.models import Goods, Orders
from easytrade.views.ViewMixIn import ViewMixIn


class BasketView(View, ViewMixIn):
    content = {}
    template_name = 'basket'
    basket = []
    order = Orders()

    def get(self, request):
        for item in request.session.get('basket', []):
            order = Orders()
            order.good = Goods.objects.get(slug=item['good'])
            order.number_of_goods = int(item['number_of_goods'])
            self.basket.append(order)
            order.save()
        self.content['basket'] = self.basket
        if 'basket' in request.session:
            del request.session['basket']

        return render(request, self.get_path(), self.content)