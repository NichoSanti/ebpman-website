# Generated by Django 4.1.2 on 2022-12-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_contact_email_address_alter_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
