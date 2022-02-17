from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.views import View

from easytrade.models import Goods, Orders
from easytrade.views.ViewMixIn import ViewMixIn


class OrderView(View, ViewMixIn):
    content = {}
    template_name = None

    def get(self, request, slug):
        good = Goods.objects.get(slug=slug)
        basket = request.session.get('basket', False) or []
        basket.append({
            'old': False,
            'good': good.slug,
            'number_of_goods': request.GET['count']
        })
        request.session['basket'] = basket
        return redirect('home')
