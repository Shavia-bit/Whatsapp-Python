# Generated by Django 4.2.5 on 2023-10-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_messagelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagelog',
            name='status',
            field=models.CharField(default='delivered', max_length=20),
        ),
    ]