# Generated by Django 3.1 on 2021-09-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0008_auto_20210902_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Payed',
            field=models.BooleanField(default=False),
        ),
    ]