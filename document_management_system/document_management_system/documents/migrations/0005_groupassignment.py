# Generated by Django 3.2.2 on 2021-05-11 11:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0004_auto_20210508_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('document', models.ManyToManyField(to='documents.Document', verbose_name='Group Document')),
                ('member', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Group User')),
            ],
        ),
    ]
