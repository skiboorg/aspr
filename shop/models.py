from django.db import models
from pytils.translit import slugify


class Manufactor(models.Model):
    name = models.CharField('Производитель', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Series(models.Model):
    name = models.CharField('Серия', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"


class Type(models.Model):
    name = models.CharField('Тип изделия', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тип изделия"
        verbose_name_plural = "Типы изделия"


class Item(models.Model):

    type = models.ForeignKey(Type, blank=True, null=True, verbose_name='Тип изделия', on_delete=models.SET_NULL,db_index=True)
    manufactor = models.ForeignKey(Manufactor, blank=True, null=True, verbose_name='Производитель', on_delete=models.SET_NULL,db_index=True)
    series = models.ForeignKey(Series, blank=True, null=True, verbose_name='Серия', on_delete=models.SET_NULL,db_index=True)
    name = models.CharField('Название товара', max_length=255, blank=True, null=True)
    option_name = models.CharField('Название товара', max_length=255, blank=True, null=True,editable=False)
    name_lower = models.CharField(max_length=255, blank=True, null=True,editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True,db_index=True,editable=False)
    price = models.IntegerField('Цена', blank=True, default=0, db_index=True)
    image = models.ImageField('Картинка', upload_to='item/', blank=True, null=True)
    page_title = models.CharField('Название страницы', max_length=255, blank=True, null=True)
    page_description = models.TextField('Описание страницы',  blank=True, null=True)
    description = models.TextField('Описание товара', blank=True, null=True)

    article = models.CharField('Артикул', max_length=50, blank=True, null=True)
    sku = models.CharField('SKU', max_length=50, blank=True, null=True)

    itemOption1Name = models.CharField('Название опции1',  max_length=255, blank=True, null=True)
    itemOption1Value = models.CharField('Значение опции1',  max_length=255, blank=True, null=True)

    itemOption2Name = models.CharField('Название опции2', max_length=255, blank=True, null=True)
    itemOption2Value = models.CharField('Значение опции2', max_length=255, blank=True, null=True)

    itemAddOption1Name = models.CharField('Название доп. опции1', max_length=255, blank=True, null=True)
    itemAddOption1Value = models.CharField('Значение доп. опции1', max_length=255, blank=True, null=True)

    itemAddOption2Name = models.CharField('Название доп. опции2', max_length=255, blank=True, null=True)
    itemAddOption2Value = models.CharField('Значение доп. опции2', max_length=255, blank=True, null=True)

    itemAddOption3Name = models.CharField('Название доп. опции3', max_length=255, blank=True, null=True)
    itemAddOption3Value = models.CharField('Значение доп. опции3', max_length=255, blank=True, null=True)

    is_active = models.BooleanField('Отображать товар ?', default=True, db_index=True)
    is_present = models.BooleanField('Товар в наличии ?', default=True, db_index=True)
    is_new = models.BooleanField('Товар новинка ?', default=False, db_index=True)

    buys = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        self.name_lower = self.name.lower()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

