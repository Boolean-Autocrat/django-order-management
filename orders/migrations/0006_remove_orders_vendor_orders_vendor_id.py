# Generated by Django 4.2.6 on 2023-10-29 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_rename_vendor_id_orders_vendor'),
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
            preserve_default=False,
        ),
    ]
