# Generated by Django 3.2.5 on 2021-08-12 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_firsname_accounts_firstname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]
