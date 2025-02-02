# Generated by Django 5.0.4 on 2024-04-17 07:38

import django.core.validators
import tasty_recipes_app.profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, message='Nickname must be at least 2 chars long!')])),
                ('first_name', models.CharField(max_length=30, validators=[tasty_recipes_app.profiles.validators.validate_name_starts_with_capital_letter])),
                ('last_name', models.CharField(max_length=30, validators=[tasty_recipes_app.profiles.validators.validate_name_starts_with_capital_letter])),
                ('chef', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
