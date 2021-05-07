# Generated by Django 3.2.1 on 2021-05-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_articlenew_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlenew',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='adress',
            field=models.CharField(choices=[('АВТОЗАВОДСКИЙ', 'Нижний Новгород, проспект Ленина, 108'), ('БУРНАКОВСКИЙ', 'Нижний Новгород, ул. Бурнаковская, 103а'), ('ДЕЛОВАЯ', 'Нижний Новгород, ул. Родионова, 201, корп. 1'), ('КОРАБЛИ', 'Нижний Новгород, пр. Кораблестроителей, д. 76')], max_length=300, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='practice',
            field=models.CharField(choices=[('US', 'LES MILLS'), ('FR', 'ВОССТАНОВИТЕЛЬНЫЙ ФИТНЕС'), ('CN', 'MIND BODY'), ('RU', 'ЕДИНОБОРСТВА'), ('IT', 'БАССЕЙН'), ('KR', 'КАРДИОТРЕНИРОВКИ')], max_length=300, verbose_name='Занятие'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='username',
            field=models.CharField(max_length=300, verbose_name='Имя'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]