# Generated by Django 3.1.5 on 2021-01-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210128_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
