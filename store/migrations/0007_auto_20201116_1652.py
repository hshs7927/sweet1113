# Generated by Django 3.1.3 on 2020-11-16 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201116_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='order_id',
            new_name='order',
        ),
    ]
