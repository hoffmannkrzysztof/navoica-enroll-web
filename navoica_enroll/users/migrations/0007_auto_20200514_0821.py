# Generated by Django 2.2.10 on 2020-05-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0006_auto_20200421_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistrationcourse',
            name='language_code',
            field=models.CharField(default='pl', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='disabled_person',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No'),
                                            ('r', 'Prefer not to tell')],
                                   max_length=1,
                                   verbose_name='Disabled person'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='education',
            field=models.CharField(
                choices=[('1', 'Pre-primary'), ('2', 'Primary'),
                         ('3', 'Secondary'), ('4', 'High school'),
                         ('5', 'Higher')], max_length=1,
                verbose_name='Education'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='homeless',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No'),
                                            ('r', 'Prefer not to tell')],
                                   max_length=1, verbose_name='Homeless'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='origin',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No'),
                                            ('r', 'Prefer not to tell')],
                                   max_length=1,
                                   verbose_name='Migrant / ethnic minority'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='profession',
            field=models.CharField(
                choices=[('Vocational teacher', 'Vocational teacher'), (
                'General education teacher', 'General education teacher'),
                         ('Kindergarten teacher', 'Kindergarten teacher'), (
                         'Employee in higher education institution',
                         'Employee in higher education institution'), (
                         'Labor market institution employee',
                         'Labor market institution employee'),
                         ('Health care worker', 'Health care worker'),
                         ('Farmer', 'Farmer'), (
                         'Key employee in social assistance and integration institution',
                         'Key employee in social assistance and integration institution'),
                         (
                         'Employee in family and foster care support institution',
                         'Employee in family and foster care support institution'),
                         ('Employee in social economy support center',
                          'Employee in social economy support center'), (
                         'Employee in psychological and pedagogical counseling center',
                         'Employee in psychological and pedagogical counseling center'),
                         ('Practical vocational instructor',
                          'Practical vocational instructor'),
                         ('Other', 'Other')], max_length=1000,
                verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='social_disadvantage',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No'),
                                            ('r', 'Prefer not to tell')],
                                   max_length=1,
                                   verbose_name='Socially disadvantaged'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='status',
            field=models.CharField(choices=[('Employed', 'Employed'), (
            'Registered unemployed', 'Registered unemployed'), (
                                            'Unregistered unemployed',
                                            'Unregistered unemployed'), (
                                            'Unemployed, not looking for work',
                                            'Unemployed, not looking for work')],
                                   max_length=1000, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='work_name',
            field=models.CharField(
                help_text='Abbreviations not allowed, full name of the institution',
                max_length=1000, verbose_name='Job title'),
        ),
    ]
