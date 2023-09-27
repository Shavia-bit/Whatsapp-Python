# Generated by Django 4.2.5 on 2023-09-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_client_address_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('whatsapp_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='deliverynote',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.clientdetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.clientdetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesorder',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.clientdetails'),
            preserve_default=False,
        ),
    ]
