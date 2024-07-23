# Generated by Django 5.0.6 on 2024-06-21 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_main_category_category_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('Availability', models.IntegerField()),
                ('featured_image', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Product_Information', models.TextField()),
                ('model_name', models.CharField(max_length=100)),
                ('Tag', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.section')),
            ],
        ),
        migrations.CreateModel(
            name='Additional_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spacification', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]