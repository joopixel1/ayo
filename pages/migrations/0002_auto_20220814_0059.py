# Generated by Django 2.1.5 on 2022-08-14 05:59

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', phone_field.models.PhoneField(help_text='Mobile phone number', max_length=31)),
                ('email', models.EmailField(help_text='email address', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bootcamp',
        ),
        migrations.RemoveField(
            model_name='cloudsite',
            name='author',
        ),
        migrations.RemoveField(
            model_name='languagesite',
            name='author',
        ),
        migrations.DeleteModel(
            name='CloudService',
        ),
        migrations.DeleteModel(
            name='CloudSite',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='LanguageSite',
        ),
    ]
