from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from easytrade.models import Goods
from easytrade.views.ViewMixIn import ViewMixIn


class GoodView(View, ViewMixIn):
    template_name = 'good'

    def get(self, request, slug):
        self.set_menu()
        self.content['good'] = Goods.objects.get(slug=slug)
        return render(request, self.get_path(), self.content)


