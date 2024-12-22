# Generated by Django 5.0.6 on 2024-12-16 17:29

import consultants_renca.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '__first__'),
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultantRenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_consultant_renca', models.CharField(default='INSCRITO', max_length=15)),
                ('type_identification_document', models.CharField(max_length=50)),
                ('identification_document', models.CharField(max_length=50)),
                ('ci_complement', models.CharField(blank=True, max_length=10, null=True)),
                ('ci_expedited', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('second_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=300)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('national_certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('state_certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.TextField()),
                ('state_certificate_doc', models.TextField(blank=True, null=True)),
                ('identification_document_doc', models.TextField(blank=True, null=True)),
                ('renca_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('request_code', models.CharField(max_length=50)),
                ('emition_date', models.DateTimeField()),
                ('consultant_type', models.CharField(max_length=50)),
                ('category', models.CharField(default='A', max_length=1)),
                ('visible_address', models.BooleanField(default=True)),
                ('visible_telephone', models.BooleanField(default=True)),
                ('visible_cellphone', models.BooleanField(default=True)),
                ('visible_email', models.BooleanField(default=True)),
                ('state', models.CharField(default='INSCRITO', max_length=50)),
                ('verification_date', models.DateTimeField(blank=True, null=True)),
                ('verified_by', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('residence_id', models.ForeignKey(blank=True, db_column='residence_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.state')),
                ('user_id', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.authuser')),
            ],
            options={
                'db_table': 'consultants_renca',
            },
        ),
        migrations.CreateModel(
            name='ConsultantExperienceRenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('organization_name', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('certificate_file', models.FileField(blank=True, null=True, upload_to=consultants_renca.models.upload_to_certificates)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('consultant', models.ForeignKey(db_column='consultant_id', on_delete=django.db.models.deletion.CASCADE, related_name='experiences_renca', to='consultants_renca.consultantrenca')),
            ],
            options={
                'db_table': 'consultant_experience_renca',
            },
        ),
        migrations.CreateModel(
            name='DepositRenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('deposit_date', models.DateTimeField()),
                ('reference_number', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('bank_account', models.ForeignKey(db_column='bank_account_id', on_delete=django.db.models.deletion.CASCADE, related_name='deposits_renca', to='parameters.bankaccount')),
                ('consultant', models.ForeignKey(db_column='consultant_id', on_delete=django.db.models.deletion.CASCADE, related_name='deposits_renca', to='consultants_renca.consultantrenca')),
            ],
            options={
                'db_table': 'deposits_renca',
            },
        ),
    ]
