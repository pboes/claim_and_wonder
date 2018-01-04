# Generated by Django 2.0 on 2017-12-12 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_auto_20171211_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.NullBooleanField()),
                ('claim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Claim')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='no_claims',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='yes_claims',
        ),
    ]
