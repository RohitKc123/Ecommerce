# Generated by Django 4.1.4 on 2022-12-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_stock'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(blank=True, choices=[('INTEL', 'INTEL'), ('AMD', 'AMD'), ('MSI', 'MSI'), ('NVIDIA', 'NVIDIA'), ('ASUS', 'ASUS')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='generation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PROCESSOR', 'PROCESSOR'), ('GRAPHICS_CARD', 'GRAPHICS_CARD'), ('RAM', 'RAM'), ('STORAGE_DEVICES', 'STORAGE_DEVICES'), ('MONITOR', 'MONITOR'), ('LAPTOP', 'LAPTOP'), ('MOTHERBOARD', 'MOTHERBOARD'), ('CASE', 'CASE'), ('POWERSUPPLY', 'POWERSUPPLY')], max_length=30),
        ),
    ]
