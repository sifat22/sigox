# Generated by Django 3.1.6 on 2021-10-07 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name': 'Contact Us From Contact Page', 'verbose_name_plural': 'Contact Us From Contact Page'},
        ),
    ]
