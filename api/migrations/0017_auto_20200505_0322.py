# Generated by Django 3.0.5 on 2020-05-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200505_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]