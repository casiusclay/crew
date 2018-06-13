from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from accounts.forms import (
    RegistationForm,
    EditProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from home.forms import HomeForm
from home.models import Post


def register(request):
    if request.method =='POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = RegistationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

@login_required()
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')


    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required()
def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/account/profile')
            else:
                return redirect('/account/change-password')
        else:
            form = PasswordChangeForm(user=request.user)
            args = {'form': form}
            return render(request, 'accounts/change_password.html', args)


@login_required()
def create_listing(request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('accounts:create_listing')

        posts = request.user.post_set.all().order_by('-created')
        return render(request, 'accounts/create-listing.html', {'posts': posts, 'form': form})


def listings(request, slug):
    listing = get_object_or_404(Post, slug=slug)

    return render(request, 'accounts/listing.html', {'listings': listing,})
