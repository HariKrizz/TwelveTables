# Generated by Django 3.2.5 on 2021-08-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_acc_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acc_data',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]