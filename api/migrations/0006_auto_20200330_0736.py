# Generated by Django 2.2.11 on 2020-03-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200330_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seo_name',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='seo_path',
            field=models.TextField(default=None, null=True),
        ),
    ]
