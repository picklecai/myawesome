# Generated by Django 3.0.6 on 2020-06-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200611_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
