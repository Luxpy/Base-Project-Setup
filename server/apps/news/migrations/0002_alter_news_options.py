# Generated by Django 4.1.3 on 2022-11-13 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at', '-updated_at'], 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
