# Generated by Django 3.0.1 on 2019-12-22 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('shape', models.CharField(max_length=50)),
                ('cake_type', models.CharField(max_length=50)),
                ('sponge', models.CharField(max_length=50)),
                ('fillings', models.CharField(max_length=50)),
                ('dietary_requirements', models.CharField(max_length=50)),
                ('creame', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('active', models.IntegerField(default='1')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('delivery_date', models.DateField(blank=True)),
                ('order_date', models.DateField()),
                ('payment_option', models.CharField(max_length=50)),
                ('order_status', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('any_other_details', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Product')),
            ],
        ),
    ]