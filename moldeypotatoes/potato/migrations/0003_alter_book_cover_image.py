# Generated by Django 3.2 on 2021-06-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0002_auto_20210630_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='potato/static/images/'),
        ),
    ]
