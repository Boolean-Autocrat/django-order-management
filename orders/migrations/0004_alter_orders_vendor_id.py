# Generated by Django 4.2.6 on 2023-10-28 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_remove_orders_vendor_orders_vendor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]