from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Recipe(models.Model):
    FRENCH = 'French'
    CHINESE = 'Chinese'
    ITALIAN = 'Italian'
    BALKAN = 'Balkan'
    OTHER = 'Other'

    CUISINE_TYPE_CHOICES = (
        (FRENCH, FRENCH),
        (CHINESE, CHINESE),
        (ITALIAN, ITALIAN),
        (BALKAN, BALKAN),
        (OTHER, OTHER),
    )

    title = models.CharField(max_length=100, validators=[MinLengthValidator(10)], unique=True,
                             null=False, blank=False)

    cuisine_type = models.CharField(max_length=7, choices=CUISINE_TYPE_CHOICES, null=False, blank=False)

    ingredients = models.TextField(help_text='Ingredients must be separated by a comma and space.',
                                   null=False, blank=False)

    instructions = models.TextField(null=False, blank=False)

    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1)],
                                               help_text='Provide the cooking time in minutes.',
                                               null=False, blank=False)

    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
