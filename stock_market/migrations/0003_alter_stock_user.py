# Generated by Django 3.2.9 on 2021-11-15 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_market', '0002_stock_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
