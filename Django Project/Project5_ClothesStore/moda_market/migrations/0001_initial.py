# Generated by Django 4.2.5 on 2023-10-08 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('category', models.CharField(choices=[('t-shirt', 'T-shirt'), ('jeans', 'Jeans'), ('short', 'Short'), ('coat', 'Coat'), ('boot', 'Boot')], max_length=10)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[('guest', 'Guest'), ('registered', 'Registered'), ('worker', 'Worker'), ('admin', 'Admin')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.CharField(max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moda_market.user')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('black', 'Black'), ('white', 'White'), ('pink', 'Pink'), ('purple', 'Purple')], max_length=10)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moda_market.item')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moda_market.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moda_market.user')),
            ],
        ),
    ]
