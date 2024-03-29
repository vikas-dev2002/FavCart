# Generated by Django 3.2.4 on 2022-09-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220903_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30)),
                ('ppic', models.ImageField(null=True, upload_to='static/profile')),
                ('passwd', models.CharField(max_length=60)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='myproduct',
            name='ppic',
            field=models.ImageField(default='', upload_to='static/category'),
        ),
    ]
