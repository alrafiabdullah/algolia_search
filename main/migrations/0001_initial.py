# Generated by Django 3.2.13 on 2022-06-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cc', models.PositiveSmallIntegerField()),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], max_length=255)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
