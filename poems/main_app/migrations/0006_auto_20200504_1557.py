# Generated by Django 3.0.4 on 2020-05-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200504_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='poem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Poem'),
        ),
    ]
