# Generated by Django 3.2.5 on 2021-07-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data',
            field=models.DateField(default='asdoasd', max_length=25),
        ),
    ]
