# Generated by Django 3.1.6 on 2021-11-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core_app', '0003_auto_20211020_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
