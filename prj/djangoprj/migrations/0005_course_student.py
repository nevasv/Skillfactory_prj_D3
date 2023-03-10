# Generated by Django 4.1.7 on 2023-02-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoprj', '0004_alter_good_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('course', models.ManyToManyField(to='djangoprj.course')),
            ],
        ),
    ]
