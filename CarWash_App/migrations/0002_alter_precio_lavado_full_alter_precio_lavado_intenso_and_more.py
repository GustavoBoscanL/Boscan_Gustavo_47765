# Generated by Django 4.2.5 on 2023-10-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarWash_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='lavado_full',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='precio',
            name='lavado_intenso',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='precio',
            name='lavado_simple',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
