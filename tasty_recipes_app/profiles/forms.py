from django import forms

from tasty_recipes_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileForm):
    class Meta(ProfileForm.Meta):
        fields = ('nickname', 'first_name', 'last_name', 'chef')


class ProfileEditForm(ProfileForm):
    pass


class ProfileDeleteForm(ProfileForm):
    class Meta(ProfileForm.Meta):
        fields = ()
