# Generated by Django 3.0.2 on 2020-02-14 02:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=None, upload_to=core.models.recipe_image_file_path),
            preserve_default=False,
        ),
    ]
