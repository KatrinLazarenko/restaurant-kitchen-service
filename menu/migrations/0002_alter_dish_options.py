# Generated by Django 4.1.3 on 2022-11-13 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['category']},
        ),
    ]