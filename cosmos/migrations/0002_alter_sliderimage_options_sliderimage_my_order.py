# Generated by Django 4.2.16 on 2024-11-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ['my_order'], 'verbose_name': 'изображение', 'verbose_name_plural': 'изображения'},
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='my_order',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
