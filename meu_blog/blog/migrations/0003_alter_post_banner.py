# Generated by Django 5.1.3 on 2024-11-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_banner_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', null=True, upload_to='posts/'),
        ),
    ]
