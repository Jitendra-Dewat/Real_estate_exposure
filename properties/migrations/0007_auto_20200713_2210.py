# Generated by Django 3.0.6 on 2020-07-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20200713_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldproperties',
            name='ac',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='soldproperties',
            name='furnshid',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='soldproperties',
            name='parking',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='soldproperties',
            name='swimmingpool',
            field=models.CharField(default=False, max_length=6),
        ),
    ]