# Generated by Django 5.0.6 on 2024-05-16 18:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(choices=[('FullTime', 'Full Time'), ('PartTime', 'Part Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=5000)),
                ('experience', models.TextField(max_length=5000)),
                ('required', models.TextField(max_length=5000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField(max_length=500)),
                ('salary', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=500)),
                ('web', models.TextField(max_length=500)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_Category', to='jobs.category')),
            ],
        ),
    ]
