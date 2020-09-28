from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from main.views import ProfilePage, RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfilePage.as_view(), name="profile"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
]
