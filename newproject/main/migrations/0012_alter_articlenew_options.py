# Generated by Django 3.2.2 on 2021-05-07 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlenew',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
