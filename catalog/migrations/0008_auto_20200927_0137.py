# Generated by Django 2.2.16 on 2020-09-27 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200927_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
    ]
