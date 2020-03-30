# Generated by Django 3.0.4 on 2020-03-30 07:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=100, unique=True)),
                ('mobile_number', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, help_text='Product name is required: It must be unique', max_length=200, unique=True)),
                ('product_description', models.CharField(db_index=True, help_text='Optional information about the product', max_length=200)),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('product_qty', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=100)),
                ('right', models.ManyToManyField(to='inventory.Right')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=200)),
                ('trade_qty', models.IntegerField(default=0)),
                ('unit_price', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('date', models.DateTimeField()),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Parner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Product')),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.User')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.User'),
        ),
        migrations.AddField(
            model_name='parner',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.User'),
        ),
    ]