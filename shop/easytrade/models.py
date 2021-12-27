import django.db.models as models


class Goods(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50, default='')
    search_queries = models.TextField(default='')
    search_queries_ukr = models.TextField(default='')
    price = models.FloatField()
    UID = models.CharField(max_length=50, default='')
    good_ID = models.CharField(max_length=50, default='')
    description = models.TextField()
    photo = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    is_trend = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField()
    goods_type = models.ForeignKey(
        'GoodTypes',
        on_delete=models.CASCADE,
        default=1
    )
    measure = models.ForeignKey(
        'Measure',
        on_delete=models.CASCADE,
        default=1
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.CASCADE,
        default=1
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

    def __str__(self):
        return str(self.pk)


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=50)

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
