# Generated by Django 2.2.5 on 2019-09-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodcare', '0002_auto_20190921_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='India', max_length=50, verbose_name='Country'),
        ),
    ]
