from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensures only logged-in users can access the profile page
def user_profile(request):
    return render(request, 'userprofile/profile.html', {'username': request.user.username})
