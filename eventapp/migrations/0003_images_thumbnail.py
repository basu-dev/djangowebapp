# Generated by Django 2.2.5 on 2019-09-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_members_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='thumbnail',
            field=models.ImageField(default='media/images/150-1.png', editable=False, upload_to='thumbnail/', verbose_name='thumbnail'),
        ),
    ]
