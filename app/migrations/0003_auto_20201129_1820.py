# Generated by Django 2.1.15 on 2020-11-29 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201129_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coverage',
            old_name='address',
            new_name='alpha1',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='age',
            new_name='alpha2',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='alpha',
            new_name='alpha3',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='name',
            new_name='category',
        ),
    ]