# Generated by Django 2.0.6 on 2018-07-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_management', '0006_auto_20180728_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployrecord',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
    ]
