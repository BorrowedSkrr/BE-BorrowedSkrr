# Generated by Django 4.2.4 on 2023-08-17 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_empolyee_is_superuser_student_is_superuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empolyee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
    ]
