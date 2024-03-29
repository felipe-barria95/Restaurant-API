# Generated by Django 3.0.5 on 2020-04-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200420_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hamburguesa_ingrediente',
            name='hamburguesa_id',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='hamburguesa_ingrediente',
            name='ingrediente_id',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False),
        ),
    ]
