# Generated by Django 4.0.4 on 2022-05-11 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.CharField(max_length=50)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(default='UnModified', max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serial', models.CharField(max_length=20, unique=True)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('standard', models.CharField(blank=True, max_length=10, null=True)),
                ('section', models.CharField(blank=True, max_length=10, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.CharField(max_length=50)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(default='UnModified', max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_code', models.CharField(max_length=20, unique=True)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]