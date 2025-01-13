from tasty_recipes_app.profiles.models import Profile


def get_last_profile():
    try:
        profile = Profile.objects.last()
    except Profile.DoesNotExist:
        profile = None
    return profile
