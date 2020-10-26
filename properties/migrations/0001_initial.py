# Generated by Django 2.1.7 on 2020-07-07 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgesofproperties',
            fields=[
                ('imageid', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='properties/forsale')),
                ('propertytype', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Imgesofrentalproperties',
            fields=[
                ('imageid', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='properties/forrent')),
                ('propertytype', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Postforrent',
            fields=[
                ('propertyid', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(default='', max_length=255)),
                ('address2', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=50)),
                ('statename', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=70)),
                ('zipf', models.CharField(default='', max_length=6)),
                ('cunstructionyear', models.CharField(default='', max_length=255)),
                ('parking', models.BooleanField(default=False)),
                ('furnshid', models.BooleanField(default=False)),
                ('ac', models.BooleanField(default=False)),
                ('swimmingpool', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=700)),
                ('rentpermonth', models.CharField(default='', max_length=12)),
                ('area', models.CharField(default='0', max_length=20)),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
                ('propertytype', models.CharField(default='', max_length=10)),
                ('mainimage', models.ImageField(default='', upload_to='properties/forsale')),
                ('maxallowedtanent', models.IntegerField(default=1)),
                ('livingtanent', models.IntegerField(default=0)),
                ('ownerid', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Postforselling',
            fields=[
                ('propertyid', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(default='', max_length=255)),
                ('address2', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=50)),
                ('statename', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=70)),
                ('zipf', models.CharField(default='', max_length=6)),
                ('cunstructionyear', models.CharField(default='', max_length=255)),
                ('parking', models.BooleanField(default=False)),
                ('furnshid', models.BooleanField(default=False)),
                ('ac', models.BooleanField(default=False)),
                ('swimmingpool', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=700)),
                ('price', models.CharField(default='', max_length=12)),
                ('area', models.CharField(default='0', max_length=20)),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
                ('propertytype', models.CharField(default='', max_length=10)),
                ('mainimage', models.ImageField(default='', upload_to='properties/forsale')),
                ('ownerid', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Soldproperties',
            fields=[
                ('oldownerid', models.CharField(default='', max_length=255)),
                ('propertyid', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(default='', max_length=255)),
                ('address2', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=50)),
                ('statename', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=70)),
                ('zipf', models.CharField(default='', max_length=6)),
                ('cunstructionyear', models.CharField(default='', max_length=255)),
                ('parking', models.BooleanField(default=False)),
                ('furnshid', models.BooleanField(default=False)),
                ('ac', models.BooleanField(default=False)),
                ('swimmingpool', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=700)),
                ('price', models.CharField(default='', max_length=12)),
                ('area', models.CharField(default='0', max_length=20)),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
                ('propertytype', models.CharField(default='', max_length=10)),
                ('mainimage', models.ImageField(default='', upload_to='properties/forsale')),
                ('solddate', models.DateTimeField(auto_now_add=True)),
                ('newownerid', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='imgesofrentalproperties',
            name='propertyid',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='properties.Postforrent'),
        ),
        migrations.AddField(
            model_name='imgesofproperties',
            name='propertyid',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='properties.Postforselling'),
        ),
    ]
