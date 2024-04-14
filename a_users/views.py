from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.


def profile_view(request):
    profile  = request.user.profile
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