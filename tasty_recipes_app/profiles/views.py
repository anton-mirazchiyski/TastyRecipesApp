from django.shortcuts import render, redirect

from tasty_recipes_app.core.utils import get_last_profile
from tasty_recipes_app.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from tasty_recipes_app.recipes.models import Recipe


def show_home_page(request):
    profile = get_last_profile()
    return render(request, 'common/home-page.html', {'profile': profile})


def create_profile(request):
    profile = get_last_profile()

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    form = ProfileCreateForm()
    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/create-profile.html', context)


def details_profile(request):
    profile = get_last_profile()
    total_recipes = Recipe.objects.all().count()
    context = {
        'profile': profile,
        'total_recipes': total_recipes,
    }

    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = get_last_profile()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    form = ProfileEditForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_last_profile()
    all_recipes = Recipe.objects.all()

    form = ProfileDeleteForm()

    if request.method == 'POST':
        profile.delete()
        all_recipes.delete()
        return redirect('home')
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', context)
