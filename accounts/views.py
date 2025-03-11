from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(f"User {user.username} registered successfully!")  # Debugging
#             login(request, user)
#             return redirect('chats')
#         else:
#             print("Form Errors:", form.errors)  # Debugging
#     else:
#         form = RegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})

from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/chats/'})  # Redirect to chats app
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # Send form errors as JSON

    form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')  # ✅ Redirects to home after logout
