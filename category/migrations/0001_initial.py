# Generated by Django 3.2.6 on 2021-08-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, unique=True)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('cart_image', models.ImageField(upload_to='categories/photos')),
            ],
        ),
    ]
