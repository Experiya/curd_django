# Generated by Django 2.1.7 on 2020-12-29 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0002_auto_20201228_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='details',
            name='first_name',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(default='', upload_to='app/images'),
        ),
        migrations.AlterField(
            model_name='details',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='details',
            name='dept',
            field=models.CharField(default='', max_length=25),
        ),
    ]
