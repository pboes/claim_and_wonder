# Generated by Django 2.0 on 2017-12-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_claim_skip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
