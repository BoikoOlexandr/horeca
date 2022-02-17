from abc import ABCMeta, abstractmethod
from easytrade.models import Categories
from easytrade.models import SuperCategory

from shop import settings


class ViewMixIn(metaclass=ABCMeta):
    content = {}

    @property
    @abstractmethod
    def template_name(self):
        pass

    def get_path(self):
        return f'easytrade/{self.template_name}.html'

    def set_menu(self):
        self.content['footer_phone'] = settings.PHONE
        self.content['super_categories'] = SuperCategory.objects.all()
        self.content['categories'] = Categories.objects.all()


