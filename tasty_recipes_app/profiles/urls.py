from django.urls import path, include

from tasty_recipes_app.profiles.views import show_home_page, create_profile, details_profile, edit_profile, \
    delete_profile

urlpatterns = [
    path('', show_home_page, name='home'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
