# Generated by Django 5.0.6 on 2024-12-18 23:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='id_module',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='id_type',
        ),
        migrations.AddField(
            model_name='announcement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='module',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
