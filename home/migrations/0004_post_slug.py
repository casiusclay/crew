# Generated by Django 2.0.5 on 2018-06-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180604_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
