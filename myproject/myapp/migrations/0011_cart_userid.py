# Generated by Django 4.0.4 on 2022-06-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cart_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userid',
            field=models.CharField(default='', max_length=100),
        ),
    ]
