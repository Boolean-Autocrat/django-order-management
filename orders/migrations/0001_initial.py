# Generated by Django 4.2.6 on 2023-10-27 13:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
