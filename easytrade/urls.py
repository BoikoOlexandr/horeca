from django.urls import path

from .views.category import CategoryView
from .views.basket import BasketView
from .views.filldb import FillDb
from .views.order import OrderView
from .views.good import GoodView
from .views.home import HomeView
from .views.search import SearchView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('good/<slug:slug>', GoodView.as_view(), name='good'),
    path('order/<slug:slug>', OrderView.as_view(), name='order'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('filldb/', FillDb.as_view(), name='filldb'),
    path('categories/<slug:category>', CategoryView.as_view(), name='cat'),
    path('search/', SearchView.as_view(), name='search')
]

