# Generated by Django 2.2 on 2021-04-29 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_contract_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contract_address',
        ),
    ]