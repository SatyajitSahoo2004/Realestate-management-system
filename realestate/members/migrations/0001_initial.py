# Generated by Django 5.1.4 on 2025-03-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=10)),
                ('password', models.CharField(default='', max_length=100)),
                ('role', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(max_length=3)),
            ],
        ),
    ]
