# Generated by Django 3.2.8 on 2021-10-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='detail',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]