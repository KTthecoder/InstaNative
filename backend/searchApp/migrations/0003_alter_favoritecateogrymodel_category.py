# Generated by Django 4.1.4 on 2023-01-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0002_favoritecateogrymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecateogrymodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryModel', to='searchApp.categoriesmodel'),
        ),
    ]
