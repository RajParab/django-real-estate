# Generated by Django 2.2.4 on 2019-08-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
