# Generated by Django 3.1 on 2021-09-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_cart_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookspurch',
            name='Seller',
        ),
        migrations.AddField(
            model_name='bookspurch',
            name='Items',
            field=models.IntegerField(null=True),
        ),
    ]