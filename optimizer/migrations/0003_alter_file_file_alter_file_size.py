# Generated by Django 5.0.4 on 2024-04-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optimizer', '0002_remove_file_name_file_file_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]