from django.shortcuts import render
from django.views import View
from easytrade.models import Goods
from easytrade.views.ViewMixIn import ViewMixIn


class HomeView(View, ViewMixIn):
    template_name = 'index'

    def get(self, request):
        self.set_menu()
        self.content['popular'] = Goods.objects.filter(is_popular=True, is_published=True)
        self.content['trends'] = Goods.objects.filter(is_trend=True, is_published=True)

        return render(request, self.get_path(), self.content)

