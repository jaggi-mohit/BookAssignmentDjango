# Generated by Django 3.1 on 2021-09-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_cart_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sum',
            field=models.IntegerField(null=True),
        ),
    ]
