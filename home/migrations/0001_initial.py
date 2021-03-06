# Generated by Django 2.1.7 on 2020-05-27 16:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profiledetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=255)),
                ('middlename', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('dob', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('address2', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=50)),
                ('statename', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=70)),
                ('zipf', models.CharField(default='', max_length=6)),
                ('image', models.ImageField(default='', upload_to='home/userprofiles')),
                ('email', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', unique=True)),
            ],
        ),
    ]
