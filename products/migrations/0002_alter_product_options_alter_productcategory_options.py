# Generated by Django 4.2.7 on 2023-11-11 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
    ]
