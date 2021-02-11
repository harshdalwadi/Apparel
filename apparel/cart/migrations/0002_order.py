# Generated by Django 3.1.4 on 2020-12-22 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_ids', models.CharField(max_length=250)),
                ('product_ids', models.CharField(max_length=250)),
                ('invoice_id', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('processed_on', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
