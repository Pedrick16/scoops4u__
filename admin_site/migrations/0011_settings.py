# Generated by Django 4.1.3 on 2023-04-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0010_cart_cart_payment_delete_pos_delete_pos_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings_category', models.CharField(max_length=250, null=True, verbose_name='Category')),
                ('settings_unit', models.CharField(max_length=250, null=True, verbose_name='Unit')),
            ],
        ),
    ]
