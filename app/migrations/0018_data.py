# Generated by Django 3.2.5 on 2021-07-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_agenda_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
            ],
        ),
    ]
