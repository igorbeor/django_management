# Generated by Django 2.2.7 on 2019-11-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workplace',
            name='name',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
