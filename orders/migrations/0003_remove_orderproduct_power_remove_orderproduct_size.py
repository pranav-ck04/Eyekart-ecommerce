# Generated by Django 4.0.6 on 2022-08-10 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='power',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
    ]
