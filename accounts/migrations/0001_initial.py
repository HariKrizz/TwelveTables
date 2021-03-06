# Generated by Django 3.2.5 on 2021-08-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firsName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('pass_wd', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('userName',),
            },
        ),
    ]
