# Generated by Django 3.1.3 on 2020-11-13 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0002_auto_20201113_2114'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_day', models.DateField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('pickuptime', models.TimeField(null=True)),
                ('picktf', models.BooleanField(null=True)),
                ('reservetf', models.BooleanField(null=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.store')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quota', models.IntegerField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('today_lineup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.today_lineup')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_insta', models.CharField(max_length=15, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
