# Generated by Django 2.1.5 on 2019-02-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='About/cover/'),
        ),
    ]
