# Generated by Django 3.2.9 on 2021-11-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product')
    ]

    operations = [
        migrations.AddIndex(
            model_name='costumer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_costu_last_na_66ca2f_idx'),
        ),
        migrations.AlterModelTable(
            name='costumer',
            table='store_costumers',
        ),
    ]
