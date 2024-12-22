# Generated by Django 5.0.6 on 2024-12-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantRenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'test',
            },
        ),
    ]
