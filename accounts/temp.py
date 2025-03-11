from django.contrib.auth.models import User

# Check if users exist
print(User.objects.all())

# Check if users are active and staff
for user in User.objects.all():
    print(user.username, user.is_active, user.is_staff, user.is_superuser)
