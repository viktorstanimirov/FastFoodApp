# Generated by Django 5.0.2 on 2024-04-06 15:07

import FastFoodApp.accounts.account_validators
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.MinLengthValidator(3), FastFoodApp.accounts.account_validators.validate_first_or_last_name_contains_only_letter, FastFoodApp.accounts.account_validators.validate_first_or_last_name_starts_with_capital_letter])),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), FastFoodApp.accounts.account_validators.validate_first_or_last_name_contains_only_letter, FastFoodApp.accounts.account_validators.validate_first_or_last_name_starts_with_capital_letter])),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='media/profile_pictures/profile_picture.png', null=True, upload_to='media/profile_pictures/')),
                ('groups', models.ManyToManyField(blank=True, related_name='appuser_set', related_query_name='appuser', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='appuser_set', related_query_name='appuser', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]