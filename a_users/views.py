from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile  = request.user.profile
        except:
            return redirect('account_login')
    context = {'profile': profile}
    return render(request, 'a_users/profile.html', context)


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False
    return render(request, 'a_users/profile_edit.html', {'form': form})