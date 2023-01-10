# Generated by Django 4.1.4 on 2023-01-02 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0005_postsubcommentmodel_commenttext_alter_postmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postcommentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biggestComment', to='homeApp.postmodel'),
        ),
    ]