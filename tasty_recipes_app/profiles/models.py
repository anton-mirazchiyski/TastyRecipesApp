from django.core.validators import MinLengthValidator
from django.db import models

from tasty_recipes_app.profiles.validators import validate_name_starts_with_capital_letter


class Profile(models.Model):
    nickname = models.CharField(max_length=20,
                                validators=[MinLengthValidator(2,
                                            message='Nickname must be at least 2 chars long!')],
                                unique=True,
                                null=False, blank=False)

    first_name = models.CharField(max_length=30, validators=[validate_name_starts_with_capital_letter],
                                  null=False, blank=False)

    last_name = models.CharField(max_length=30, validators=[validate_name_starts_with_capital_letter],
                                 null=False, blank=False)

    chef = models.BooleanField(default=False, null=False, blank=False)

    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname
