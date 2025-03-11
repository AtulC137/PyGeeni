from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include
from .views import custom_logout  # ✅ Import the custom logout function
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('chats/', include('chats.urls')),
    path('logout/', custom_logout, name='logout'),  # ✅ Use custom logout
]

