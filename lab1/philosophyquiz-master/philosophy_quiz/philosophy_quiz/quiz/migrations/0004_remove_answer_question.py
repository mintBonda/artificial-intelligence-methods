# Generated by Django 3.1.3 on 2021-04-06 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210406_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]
