# Generated by Django 2.2.10 on 2020-02-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_userregistrationcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='street',
            field=models.CharField(max_length=300),
        ),
    ]
