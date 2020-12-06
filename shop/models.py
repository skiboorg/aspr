from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from random import choices
import string

class Category(models.Model):
    name = models.CharField('Категория', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Картинка', upload_to='category/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        self.name_lower = self.name.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,
                                 verbose_name='Относится к ',related_name='subcats')
    name = models.CharField('Подкатегория', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Картинка', upload_to='subcategory/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        self.name_lower = self.name.lower()
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Manufactor(models.Model):
    name = models.CharField('Производитель', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Относится к ')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Относится к ')
    manufactor = models.ForeignKey(Manufactor, blank=True, null=True, verbose_name='Производитель', on_delete=models.SET_NULL,db_index=True)
    name = models.CharField('Название товара', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True,editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True,db_index=True,editable=False)
    price = models.IntegerField('Цена', blank=True, default=0, db_index=True)
    image = models.ImageField('Картинка', upload_to='item/', blank=True, null=True)
    page_title = models.CharField('Название страницы', max_length=255, blank=True, null=True)
    page_description = models.TextField('Описание страницы',  blank=True, null=True)
    description = models.TextField('Описание товара', blank=True, null=True)
    article = models.CharField('Артикул', max_length=50, blank=True, null=True)
    full_description = RichTextUploadingField('Полное описание',blank=True, null=True)

    pump_count = models.IntegerField('Кол-во насосов', default=0)
    pump_power = models.CharField('(Мощность насоса, кВт',  max_length=255, blank=True, null=True)
    privod_type = models.CharField('Тип привода',  max_length=255, blank=True, null=True)

    engine_count = models.IntegerField('Кол-во двигателей', default=0)
    engine_power = models.IntegerField('Мощность двигателя, кВт', default=0)
    engine_tok = models.IntegerField('Ток двигателя', default=0)
    engine_start = models.CharField('Способ запуска двигателя',  max_length=255, blank=True, null=True)
    is_counters = models.BooleanField('Наличие счетчиков', default=False)
    number_zadvigek = models.IntegerField('Кол-во задвижек', default=0)

    inputs = models.IntegerField('Кол-во вводов', default=0)
    nominal_tok = models.IntegerField('Номинальный ток', default=0)
    is_avr = models.BooleanField('Наличие АВР',default=False)


    defence = models.CharField('Степень защиты, IP',  max_length=255, blank=True, null=True)
    setup_type = models.CharField('Способ установки',  max_length=255, blank=True, null=True)
    size_shelter = models.CharField('Размер шкафа ШхГхВ',  max_length=255, blank=True, null=True)
    warranty = models.CharField('Гарантия',  max_length=255, blank=True, null=True)
    life_time = models.CharField('Срок эксплуатации',  max_length=255, blank=True, null=True)
    work_type = models.CharField('Режим работы',  max_length=255, blank=True, null=True)
    work_temperature = models.CharField('Температурный режим',  max_length=255, blank=True, null=True)
    parametr_check = models.CharField('Контроль параметров',  max_length=255, blank=True, null=True)
    kabel_input = models.CharField('Кабельный ввод',  max_length=255, blank=True, null=True)
    power = models.CharField('Параметр: Мощность, кВт',  max_length=255, blank=True, null=True)
    tok_str = models.CharField('Параметр: Сила тока, А',  max_length=255, blank=True, null=True)
    faz_number = models.CharField('Параметр: Количество фаз',  max_length=255, blank=True, null=True)
    series = models.CharField('Параметр: Серия',  max_length=255, blank=True, null=True)
    napryag = models.CharField('Параметр: Напряжение, В',  max_length=255, blank=True, null=True)
    number_faz = models.CharField('Параметр: Количество фаз',  max_length=255, blank=True, null=True)



    is_active = models.BooleanField('Отображать товар ?', default=True, db_index=True)
    is_present = models.BooleanField('Товар в наличии ?', default=True, db_index=True)
    is_new = models.BooleanField('Товар новинка ?', default=False, db_index=True)

    buys = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_lower = self.name.lower()
        testSlug = Item.objects.filter(name_slug=slug)
        slugRandom = ''
        if testSlug:
            slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=3))
        self.name_slug = slug + slugRandom
        super(Item, self).save(*args, **kwargs)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return 'http://placehold.it/300'

    def get_absolute_url(self):
        return f'/catalog/items/{self.name_slug}/'

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

