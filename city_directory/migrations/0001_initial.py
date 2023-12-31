# Generated by Django 4.2.4 on 2023-08-14 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone number')),
                ('second_phone', models.CharField(max_length=12, verbose_name='Phone number')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('photo', models.ImageField(upload_to='city_directory.Image', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['mail'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='city_directory.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=150, verbose_name='Description')),
                ('address', models.CharField(max_length=120, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogs', to='city_directory.category')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogs', to='city_directory.contact')),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
                'ordering': ['name', 'city'],
            },
        ),
    ]
