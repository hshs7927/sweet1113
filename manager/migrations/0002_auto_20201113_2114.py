# Generated by Django 3.1.3 on 2020-11-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='biz_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='biz_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='biz_url',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
