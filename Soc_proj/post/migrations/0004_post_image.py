# Generated by Django 4.1.7 on 2023-05-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/', verbose_name='Картинка'),
        ),
    ]
