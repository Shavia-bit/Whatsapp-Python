# Generated by Django 4.2.5 on 2023-10-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_clientdata_value_clientdata_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='id_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='wa_number',
            field=models.CharField(max_length=15),
        ),
    ]
