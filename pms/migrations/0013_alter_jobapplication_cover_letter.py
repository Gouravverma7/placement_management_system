# Generated by Django 4.1 on 2023-10-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0012_alter_jobapplication_cover_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(),
        ),
    ]
