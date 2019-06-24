# Generated by Django 2.2.2 on 2019-06-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='test',
            name='birthtime',
            field=models.DateField(default='2015-01-01'),
        ),
        migrations.AddField(
            model_name='test',
            name='gender',
            field=models.CharField(default='男', max_length=2),
        ),
    ]