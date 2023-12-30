# Generated by Django 5.0 on 2023-12-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console_user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200, unique=True)),
                ('role_description', models.TextField(blank=True, null=True)),
                ('role_expiry', models.DateTimeField()),
            ],
        ),
    ]