# Generated by Django 4.2.4 on 2023-08-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0008_rename_categroy_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='isAllowed',
            field=models.BooleanField(default=False),
        ),
    ]
