from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify


class HomePage(models.Model):
    banner_img = models.ImageField('Баннер', upload_to='banner/',blank=True,null=True)
    banner_text = RichTextUploadingField(
        'Текст на баннер',
        blank=True, null=True)
    page_title = models.CharField('Заголовок страницы (Тег Titlе)', max_length=255, default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация')
    page_description = models.TextField('Описание страницы (Тег Description)', blank=True,null=True)
    block1 = models.CharField('Заголовок блока1', max_length=255, default='Направления деятельности')
    block2 = models.CharField('Заголовок блока2', max_length=255, default='Производство')
    block2_text = models.TextField('Тест блока2', default='АСПР Групп предоставляет услуги по проектированию и производству следующего электрооборудования:')
    block3 = models.CharField('Заголовок блока3', max_length=255, default='Нам доверяют')
    block4 = models.CharField('Заголовок блока4', max_length=255, default='Мы предлагаем своим клиентам')


    def __str__(self):
        return f'Главная страница'

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"


class Block1Item(models.Model):
    page = models.ForeignKey(HomePage,on_delete=models.SET_NULL,blank=True,null=True,related_name='block1items')
    icon = models.ImageField('Иконка', upload_to='block1/', blank=True, null=True)
    name = models.CharField('Название ', max_length=255, blank=True,null=True)
    text = models.TextField('Описание ', blank=True,null=True)

    def __str__(self):
        return f'Элемент блока1 - {self.name}'

    class Meta:
        verbose_name = "Элемент блока1"
        verbose_name_plural = "Элементы блока1"

class Manufactory(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.SET_NULL, blank=True, null=True,related_name='manufactoryitems')
    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    content = RichTextUploadingField('Содержимое страницы', blank=True, null=True)
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        self.name_lower = self.name.lower()
        super(Manufactory, self).save(*args, **kwargs)

    def __str__(self):
        return f'Элемент блока производство - {self.name}'

    def get_absolute_url(self):
        return f'/proizvodstvo/{self.name_slug}/'

    class Meta:
        verbose_name = "Элемент блока производство"
        verbose_name_plural = "Элементы блока производство"

class Partner(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.SET_NULL, blank=True, null=True,related_name='partneritems')
    image = models.ImageField('Изображение', upload_to='partner/', blank=True, null=True)

    def __str__(self):
        return f'Элемент блока нам доверяют'

    class Meta:
        verbose_name = "Элемент блока нам доверяют"
        verbose_name_plural = "Элементы блока нам доверяют"

class Feature(models.Model):
    page = models.ForeignKey(HomePage, on_delete=models.SET_NULL, blank=True, null=True,related_name='featureitems')
    name = models.CharField('Название ', max_length=255, blank=True,null=True)
    text = models.TextField('Описание ', blank=True,null=True)

    def __str__(self):
        return f'Элемент мы предлагаем  - {self.name}'

    class Meta:
        verbose_name = "Элемент блока мы предлагаем"
        verbose_name_plural = "Элементы блока мы предлагаем"


class AvtomatizaciyaPage(models.Model):
    page_title = models.CharField('Заголовок страницы (Тег Titlе)', max_length=255,
                                  default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация')
    page_description = models.TextField('Описание страницы (Тег Description)', blank=True, null=True)
    content = RichTextUploadingField('Содержимое страницы',blank=True, null=True)

    def __str__(self):
        return f'Страница автоматизация'

    class Meta:
        verbose_name = "Страница автоматизация"
        verbose_name_plural = "Страница автоматизация"

class ProizvodsvoPage(models.Model):
    page_title = models.CharField('Заголовок страницы (Тег Titlе)', max_length=255,
                                  default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация')
    page_description = models.TextField('Описание страницы (Тег Description)', blank=True, null=True)
    content = RichTextUploadingField('Содержимое страницы',blank=True, null=True)
    def __str__(self):
        return f'Страница производство'

    class Meta:
        verbose_name = "Страница производство"
        verbose_name_plural = "Страница производство"

class Project(models.Model):
    icon = models.ImageField('Картинка', upload_to='projects/', blank=True, null=True)
    date = models.CharField('Дата изготовления', max_length=255, blank=True,null=True)
    name = models.CharField('Название ', max_length=255, blank=True,null=True)
    text = models.TextField('Описание ', blank=True,null=True)

    def __str__(self):
        return f'Проект - {self.name}'

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class WorkTypePage(models.Model):
    page_title = models.CharField('Заголовок страницы (Тег Titlе)', max_length=255,
                                  default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация')
    page_description = models.TextField('Описание страницы (Тег Description)', blank=True, null=True)
    title = models.CharField('заголовок (H1)', max_length=255, default='Направления компании')
    text = models.TextField('Описание ', default='Компания создает системы АСУТП и электроснабжения для различных технологических установок.<br>'
                                                 'Для получения детальной информации свяжитесь с нами.<br>'
                                                 'Наши решения поставляются на заводы ПАО «НК «Роснефть», ПАО "Газпром", ГУП «Водоканал Санкт-Петербурга» и другие.<br>'
                                                 'Ниже представлены основные объекты для создания систем АСУТП и электроснабжения.')
    def __str__(self):
        return f'Страница направления'

    class Meta:
        verbose_name = "Страница направления"
        verbose_name_plural = "Страница направления"

class WorkType(models.Model):
    page = models.ForeignKey(WorkTypePage, on_delete=models.SET_NULL, blank=True, null=True, related_name='wortypes')
    image = models.ImageField('Картинка', upload_to='projects/', blank=True, null=True)
    name = models.CharField('Название ', max_length=255, blank=True,null=True)


    def __str__(self):
        return f'Направление - {self.name}'

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

class AboutPage(models.Model):
    page_title = models.CharField('Заголовок страницы (Тег Titlе)', max_length=255,
                                  default='АСПР Групп | Санкт-Петербург | Промышленная автоматизация')
    page_description = models.TextField('Описание страницы (Тег Description)', blank=True, null=True)
    content = RichTextUploadingField('Содержимое страницы',blank=True, null=True)
    def __str__(self):
        return f'Страница о нас'

    class Meta:
        verbose_name = "Страница о нас"
        verbose_name_plural = "Страница о нас"
