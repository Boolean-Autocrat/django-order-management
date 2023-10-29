# Generated by Django 4.2.6 on 2023-10-28 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_orders_vendor_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='vendor',
        ),
        migrations.AddField(
            model_name='orders',
            name='vendor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
