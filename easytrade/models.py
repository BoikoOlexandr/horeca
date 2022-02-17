import django.db.models as models
from django_extensions.db.fields import AutoSlugField as autoSlugField

class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    code = models.CharField(max_length=50, default='', verbose_name='Артикул старий')
    articul = models.CharField(max_length=50, default='0', verbose_name='Артикул')
    search_queries = models.TextField(default='', verbose_name='Пошукові запити')
    search_queries_ukr = models.TextField(default='', verbose_name='Пошукові запити(укр)')
    price = models.FloatField(verbose_name='"Чиста" ціна')
    end_price = models.FloatField(default=0, verbose_name='Ціна')
    UID = models.CharField(max_length=50, default='')
    good_ID = models.CharField(max_length=50, default='')
    description = models.TextField(verbose_name='Опис')
    photo = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото товару')
    created = models.DateTimeField(auto_now_add=True)
    is_trend = models.BooleanField(default=False, verbose_name='В тренди')
    is_popular = models.BooleanField(default=False, verbose_name='В популярні')
    is_published = models.BooleanField(default=False, verbose_name='Публікувати')
    slug = models.SlugField()
    goods_type = models.ForeignKey(
        'GoodTypes',
        on_delete=models.CASCADE,
        default=1
    )
    measure = models.ForeignKey(
        'Measure',
        on_delete=models.CASCADE,
        default=1,
        verbose_name='Одиниці виміру'
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
        default=1,
        verbose_name='Категорія'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товари'


class Orders(models.Model):
    number_of_goods = models.IntegerField()
    good = models.ForeignKey(
        'Goods',
        on_delete=models.CASCADE,
    )
    session_id = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.pk} -> {self.good.title} {self.number_of_goods}  штук "


class Baskets(models.Model):
    status = models.CharField(max_length=50)
    orders = models.ManyToManyField('Orders')
    address = models.CharField(max_length=400, default='')
    description = models.CharField(max_length=400, default='')
    telephone = models.CharField(max_length=15, default='')
    user_name = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.pk)


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    super_category = models.ForeignKey(
        'SuperCategory',
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GoodTypes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SuperCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='uploads/supercategory/')

    def __str__(self):
        return self.name
