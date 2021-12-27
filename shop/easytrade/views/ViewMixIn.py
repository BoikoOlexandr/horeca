from abc import ABCMeta, abstractmethod
from easytrade.models import Categories


class ViewMixIn(metaclass=ABCMeta):
    content = {}

    @property
    @abstractmethod
    def template_name(self):
        pass

    def get_path(self):
        return f'easytrade/{self.template_name}.html'

    def set_menu(self):
        self.content['categories'] = Categories.objects.all()
