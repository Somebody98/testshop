# Generated by Django 5.0.2 on 2024-03-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svyaz',
            name='datetime',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='svyaz',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='svyaz',
            name='number',
            field=models.TextField(),
        ),
    ]