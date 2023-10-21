# Generated by Django 4.1 on 2023-10-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0009_companyprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='company_profile_pics/'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_profile_pics/'),
        ),
    ]
