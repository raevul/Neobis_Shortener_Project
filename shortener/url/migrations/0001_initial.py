# Generated by Django 5.0.1 on 2024-01-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_link', models.URLField(verbose_name='URL')),
                ('short_link', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
        ),
    ]
