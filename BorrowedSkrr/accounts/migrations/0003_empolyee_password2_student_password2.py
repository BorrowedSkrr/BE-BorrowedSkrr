# Generated by Django 4.2 on 2023-08-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_empolyee_schoolcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='empolyee',
            name='password2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
