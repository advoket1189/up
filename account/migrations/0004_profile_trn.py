# Generated by Django 2.1.3 on 2019-06-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190527_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='TRN',
            field=models.CharField(default=1, max_length=9),
        ),
    ]
