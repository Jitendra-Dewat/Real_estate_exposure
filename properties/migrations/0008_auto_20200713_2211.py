# Generated by Django 3.0.6 on 2020-07-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20200713_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postforrent',
            name='ac',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='postforrent',
            name='furnshid',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='postforrent',
            name='parking',
            field=models.CharField(default=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='postforrent',
            name='swimmingpool',
            field=models.CharField(default=False, max_length=6),
        ),
    ]
