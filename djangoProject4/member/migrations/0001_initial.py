# Generated by Django 3.2.11 on 2022-01-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memberTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200)),
                ('userpw', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('usertel', models.CharField(max_length=200)),
            ],
        ),
    ]
