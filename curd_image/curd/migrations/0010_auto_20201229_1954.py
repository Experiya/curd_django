# Generated by Django 2.1.7 on 2020-12-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0009_auto_20201229_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(default='', upload_to='app/images'),
        ),
    ]
