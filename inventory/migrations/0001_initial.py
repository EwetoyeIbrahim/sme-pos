# Generated by Django 3.0.4 on 2020-04-02 17:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, help_text='Product name is required: It must be unique', max_length=200, unique=True)),
                ('product_description', models.CharField(blank=True, db_index=True, help_text='Optional information about the product', max_length=200)),
                ('product_code', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('product_qty', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
