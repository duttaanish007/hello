# Generated by Django 4.1.7 on 2023-03-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('pwd', models.CharField(max_length=50)),
                ('pwd2', models.CharField(max_length=50)),
            ],
        ),
    ]
