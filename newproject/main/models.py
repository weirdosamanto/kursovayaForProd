import datetime
from django.db import models



class ArticleNew(models.Model):
    """Model definition for ArticleNew."""
    article_title = models.CharField("Название статьи", max_length=200)
    article_text = models.TextField("Текст статьи")
    pub_date = models.DateTimeField("Дата публикации", auto_now=False, auto_now_add=False)
    image = models.ImageField("Изображение", null=True, upload_to='media', height_field=None, width_field=None, max_length=None)


    class Meta:
        """Meta definition for ArticleNew."""
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self):
        """Unicode representation of ArticleNew."""
        return self.article_title



class Articles(models.Model):
    CHOICES = (
        ('US', 'LES MILLS'),
        ('FR', 'ВОССТАНОВИТЕЛЬНЫЙ ФИТНЕС'),
        ('CN', 'MIND BODY'),
        ('RU', 'ЕДИНОБОРСТВА'),
        ('IT', 'БАССЕЙН'),
        ('KR', 'КАРДИОТРЕНИРОВКИ'),
    )

    ChoisesAdress = (
        ('АВТОЗАВОДСКИЙ', 'Нижний Новгород, проспект Ленина, 108'),
        ('БУРНАКОВСКИЙ', 'Нижний Новгород, ул. Бурнаковская, 103а'),
        ('ДЕЛОВАЯ', 'Нижний Новгород, ул. Родионова, 201, корп. 1'),
        ('КОРАБЛИ', 'Нижний Новгород, пр. Кораблестроителей, д. 76'),
    )



    username = models.CharField("Имя", max_length=300)
    email = models.CharField("Email", max_length=50)
    practice = models.CharField("Занятие", max_length=300, choices = CHOICES)
    adress = models.CharField("Адрес", max_length=300, choices = ChoisesAdress)
    date = models.DateTimeField(" Дата")


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Регистрация на занятие"
        verbose_name_plural = 'Регистрации на занятия'
